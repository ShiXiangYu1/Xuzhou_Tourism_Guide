/**
 * 徐州旅游攻略 - 地图工具函数测试
 * 测试使用Mocha和Chai
 */

describe('地图工具函数测试', function() {
    // 保存原始方法，以便测试后恢复
    const originalConsoleError = console.error;
    const originalWindowOpen = window.open;
    
    // 在每个测试之前设置DOM和模拟
    beforeEach(function() {
        // 创建测试DOM
        document.body.innerHTML = `
            <button id="test-nav-btn" class="map-nav-btn" 
                data-name="测试位置" 
                data-address="测试地址" 
                data-lat="34.26" 
                data-lng="117.2">
                导航
            </button>
        `;
        
        // 模拟window.open方法
        window.open = function(url, target) {
            // 仅记录调用，不实际打开窗口
            window.lastOpenedUrl = url;
            window.lastOpenedTarget = target;
        };
        
        // 模拟console.error方法
        console.error = function(message) {
            // 记录错误信息但不输出
            window.lastErrorMessage = message;
        };
    });
    
    // 在每个测试之后恢复原始方法
    afterEach(function() {
        // 清理测试DOM
        document.body.innerHTML = '';
        
        // 恢复原始方法
        console.error = originalConsoleError;
        window.open = originalWindowOpen;
        
        // 清除记录的信息
        window.lastOpenedUrl = null;
        window.lastOpenedTarget = null;
        window.lastErrorMessage = null;
        
        // 移除可能创建的下拉菜单
        const dropdown = document.querySelector('.map-dropdown');
        if (dropdown) dropdown.remove();
    });
    
    // 测试初始化方法
    describe('initMapNavigation()', function() {
        it('应该为导航按钮添加点击事件', function() {
            // 初始化导航功能
            initMapNavigation();
            
            // 获取按钮并触发点击
            const button = document.querySelector('#test-nav-btn');
            const clickEvent = new MouseEvent('click', {
                bubbles: true,
                cancelable: true
            });
            
            // 创建一个间谍函数来检测openMapNavigation是否被调用
            let openMapNavigationCalled = false;
            const originalOpenMapNav = window.openMapNavigation;
            window.openMapNavigation = function() {
                openMapNavigationCalled = true;
            };
            
            // 触发点击事件
            button.dispatchEvent(clickEvent);
            
            // 恢复原始函数
            window.openMapNavigation = originalOpenMapNav;
            
            // 断言间谍函数被调用
            chai.expect(openMapNavigationCalled).to.be.true;
        });
    });
    
    // 测试导航方法
    describe('导航方法', function() {
        describe('navigateBaiduMap()', function() {
            it('应该使用坐标打开百度地图', function() {
                // 调用带坐标的百度地图导航
                navigateBaiduMap('34.26', '117.2', '测试位置', '测试地址');
                
                // 验证正确的URL被打开
                chai.expect(window.lastOpenedUrl).to.include('api.map.baidu.com/marker');
                chai.expect(window.lastOpenedUrl).to.include('34.26,117.2');
                chai.expect(window.lastOpenedUrl).to.include('测试位置');
                chai.expect(window.lastOpenedTarget).to.equal('_blank');
            });
            
            it('应该使用关键词打开百度地图（无坐标）', function() {
                // 调用不带坐标的百度地图导航
                navigateBaiduMap(null, null, '测试位置', '测试地址');
                
                // 验证正确的URL被打开
                chai.expect(window.lastOpenedUrl).to.include('map.baidu.com/search');
                chai.expect(window.lastOpenedUrl).to.include('测试位置');
                chai.expect(window.lastOpenedUrl).to.include('测试地址');
                chai.expect(window.lastOpenedTarget).to.equal('_blank');
            });
            
            it('应该处理异常情况', function() {
                // 模拟抛出异常的情况
                window.open = function() {
                    throw new Error('测试错误');
                };
                
                // 调用方法应该捕获错误而不抛出
                chai.expect(function() {
                    navigateBaiduMap('34.26', '117.2', '测试位置', '测试地址');
                }).to.not.throw();
                
                // 验证错误被记录
                chai.expect(window.lastErrorMessage).to.include('百度地图导航出错');
            });
        });
        
        describe('navigateAMap()', function() {
            it('应该使用坐标打开高德地图', function() {
                // 调用高德地图导航
                navigateAMap('34.26', '117.2', '测试位置', '测试地址');
                
                // 验证正确的URL被打开
                chai.expect(window.lastOpenedUrl).to.include('uri.amap.com/marker');
                chai.expect(window.lastOpenedUrl).to.include('117.2,34.26');
                chai.expect(window.lastOpenedUrl).to.include('测试位置');
                chai.expect(window.lastOpenedTarget).to.equal('_blank');
            });
        });
        
        describe('navigateTencentMap()', function() {
            it('应该使用坐标打开腾讯地图', function() {
                // 调用腾讯地图导航
                navigateTencentMap('34.26', '117.2', '测试位置', '测试地址');
                
                // 验证正确的URL被打开
                chai.expect(window.lastOpenedUrl).to.include('map.qq.com/coord');
                chai.expect(window.lastOpenedUrl).to.include('117.2,34.26');
                chai.expect(window.lastOpenedUrl).to.include('测试位置');
                chai.expect(window.lastOpenedTarget).to.equal('_blank');
            });
        });
    });
    
    // 测试导航菜单
    describe('openMapNavigation()', function() {
        it('应该创建导航下拉菜单', function() {
            // 触发导航菜单
            const mockEvent = {
                preventDefault: function() {},
                stopPropagation: function() {},
                clientX: 100,
                clientY: 100
            };
            
            openMapNavigation(mockEvent, '测试位置', '测试地址', '34.26', '117.2');
            
            // 检查下拉菜单是否被创建
            const dropdown = document.querySelector('.map-dropdown');
            chai.expect(dropdown).to.not.be.null;
            
            // 检查菜单内容
            const title = dropdown.querySelector('.map-dropdown-title');
            chai.expect(title.textContent).to.include('测试位置');
            
            // 检查菜单选项
            const items = dropdown.querySelectorAll('.map-nav-item');
            chai.expect(items.length).to.be.at.least(3); // 至少应有百度、高德、腾讯三个选项
        });
        
        it('应该处理缺失参数', function() {
            // 不提供地点名称应该显示错误
            openMapNavigation(null, null, '测试地址', '34.26', '117.2');
            
            // 验证没有创建下拉菜单
            const dropdown = document.querySelector('.map-dropdown');
            chai.expect(dropdown).to.be.null;
            
            // 验证错误被记录
            chai.expect(window.lastErrorMessage).to.include('导航信息不完整');
        });
        
        it('应该在点击导航选项时调用对应的导航方法', function() {
            // 创建导航菜单
            openMapNavigation(null, '测试位置', '测试地址', '34.26', '117.2');
            
            // 找到百度地图选项并点击
            const baiduOption = Array.from(document.querySelectorAll('.map-nav-item'))
                .find(el => el.textContent.includes('百度地图'));
            
            // 记录navigateBaiduMap是否被调用
            let baiduMapCalled = false;
            const originalBaiduNav = window.navigateBaiduMap;
            window.navigateBaiduMap = function() {
                baiduMapCalled = true;
            };
            
            // 点击选项
            baiduOption.click();
            
            // 恢复原始函数
            window.navigateBaiduMap = originalBaiduNav;
            
            // 验证方法被调用
            chai.expect(baiduMapCalled).to.be.true;
            
            // 验证下拉菜单被移除
            const dropdown = document.querySelector('.map-dropdown');
            chai.expect(dropdown).to.be.null;
        });
    });
});

// 如果在Node环境中运行，导出测试
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initMapNavigation,
        navigateBaiduMap,
        navigateAMap,
        navigateTencentMap,
        openMapNavigation
    };
} 