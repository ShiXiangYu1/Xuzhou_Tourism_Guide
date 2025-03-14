/**
 * 徐州旅游攻略 - 地图工具函数
 * 用于提供精确的地图导航功能
 * 支持百度地图、高德地图、腾讯地图等多种导航方式
 * 优化移动端体验和错误处理
 */

// 记录已创建的下拉菜单，用于防止重复创建
let activeMapDropdown = null;

// 当DOM加载完成后初始化地图功能
document.addEventListener('DOMContentLoaded', function() {
    initMapNavigation();
});

/**
 * 初始化地图导航功能
 * 为所有带有经纬度数据的导航按钮添加点击事件
 */
function initMapNavigation() {
    // 获取所有导航按钮
    const navButtons = document.querySelectorAll('.map-nav-btn');
    
    // 为每个按钮添加点击事件
    navButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // 获取数据属性
            const lat = this.getAttribute('data-lat');
            const lng = this.getAttribute('data-lng');
            const name = this.getAttribute('data-name');
            const address = this.getAttribute('data-address');
            
            // 打开导航菜单
            openMapNavigation(e, name, address, lat, lng);
        });
    });
    
    // 为文档添加点击事件，点击其他区域关闭导航菜单
    document.addEventListener('click', function(e) {
        if (activeMapDropdown && !activeMapDropdown.contains(e.target)) {
            activeMapDropdown.remove();
            activeMapDropdown = null;
        }
    });
    
    // 在窗口大小改变时关闭导航菜单
    window.addEventListener('resize', function() {
        if (activeMapDropdown) {
            activeMapDropdown.remove();
            activeMapDropdown = null;
        }
    });
}

/**
 * 使用百度地图导航
 * @param {string} lat - 纬度
 * @param {string} lng - 经度
 * @param {string} name - 地点名称
 * @param {string} address - 地址信息
 */
function navigateBaiduMap(lat, lng, name, address) {
    try {
        // 有坐标时，直接使用坐标导航
        if (lat && lng) {
            const url = `https://api.map.baidu.com/marker?location=${lat},${lng}&title=${encodeURIComponent(name)}&content=${encodeURIComponent(address || '')}&output=html&src=webapp.baidu.openAPIdemo`;
            window.open(url, '_blank');
        } 
        // 无坐标时，使用关键词搜索
        else {
            const region = '徐州市';
            const keyword = address ? `${name} ${address}` : name;
            const url = `https://map.baidu.com/search/${encodeURIComponent(region + keyword)}/?querytype=s&wd=${encodeURIComponent(region + keyword)}`;
            window.open(url, '_blank');
        }
    } catch (error) {
        console.error('百度地图导航出错:', error);
        showNavigationError('百度地图导航失败，请稍后重试');
    }
}

/**
 * 使用高德地图导航
 * @param {string} lat - 纬度
 * @param {string} lng - 经度
 * @param {string} name - 地点名称
 * @param {string} address - 地址信息
 */
function navigateAMap(lat, lng, name, address) {
    try {
        // 构建搜索关键词
        const keyword = `${name} ${address || ''}`;
        
        // 构建URL
        let url = `https://uri.amap.com/search?keyword=${encodeURIComponent(keyword)}&city=徐州`;
        
        // 如果有经纬度，加上坐标
        if (lat && lng) {
            // 需要转换为高德坐标系（暂简单处理，实际使用需精确转换）
            url = `https://uri.amap.com/marker?position=${lng},${lat}&name=${encodeURIComponent(name)}&src=mypage&coordinate=gaode`;
        }
        
        window.open(url, '_blank');
    } catch (error) {
        console.error('高德地图导航出错:', error);
        showNavigationError('高德地图导航失败，请稍后重试');
    }
}

/**
 * 使用腾讯地图导航
 * @param {string} lat - 纬度
 * @param {string} lng - 经度
 * @param {string} name - 地点名称
 * @param {string} address - 地址信息
 */
function navigateTencentMap(lat, lng, name, address) {
    try {
        // 构建完整地址
        const fullAddress = `徐州市 ${address || name}`;
        
        // 构建URL
        let url = `https://map.qq.com/search?keyword=${encodeURIComponent(fullAddress)}`;
        
        // 如果有经纬度，加上坐标
        if (lat && lng) {
            url = `https://map.qq.com/coord/${lng},${lat}/${encodeURIComponent(name)}`;
        }
        
        window.open(url, '_blank');
    } catch (error) {
        console.error('腾讯地图导航出错:', error);
        showNavigationError('腾讯地图导航失败，请稍后重试');
    }
}

/**
 * 使用Apple地图导航（iOS设备）
 * @param {string} lat - 纬度
 * @param {string} lng - 经度
 * @param {string} name - 地点名称
 * @param {string} address - 地址信息
 */
function navigateAppleMap(lat, lng, name, address) {
    try {
        // 构建URL
        let url;
        
        if (lat && lng) {
            // 有坐标时使用坐标
            url = `https://maps.apple.com/?ll=${lat},${lng}&q=${encodeURIComponent(name)}`;
        } else {
            // 无坐标时使用地址搜索
            const fullAddress = `${name} ${address || ''} 徐州市`;
            url = `https://maps.apple.com/?q=${encodeURIComponent(fullAddress)}`;
        }
        
        window.open(url, '_blank');
    } catch (error) {
        console.error('Apple地图导航出错:', error);
        showNavigationError('Apple地图导航失败，请稍后重试');
    }
}

/**
 * 使用Google地图导航
 * @param {string} lat - 纬度
 * @param {string} lng - 经度
 * @param {string} name - 地点名称
 * @param {string} address - 地址信息
 */
function navigateGoogleMap(lat, lng, name, address) {
    try {
        // 构建URL
        let url;
        
        if (lat && lng) {
            // 有坐标时使用坐标
            url = `https://www.google.com/maps/search/?api=1&query=${lat},${lng}&query_place_id=${encodeURIComponent(name)}`;
        } else {
            // 无坐标时使用地址搜索
            const fullAddress = `${name} ${address || ''} 徐州市 中国`;
            url = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(fullAddress)}`;
        }
        
        window.open(url, '_blank');
    } catch (error) {
        console.error('Google地图导航出错:', error);
        showNavigationError('Google地图导航失败，请稍后重试');
    }
}

/**
 * 显示导航错误消息
 * @param {string} message - 错误信息
 */
function showNavigationError(message) {
    if (typeof message !== 'string' || !message) {
        message = '导航功能出错，请稍后重试';
    }
    
    // 创建错误提示元素
    const errorEl = document.createElement('div');
    errorEl.className = 'alert alert-danger map-nav-error';
    errorEl.style.position = 'fixed';
    errorEl.style.bottom = '20px';
    errorEl.style.left = '50%';
    errorEl.style.transform = 'translateX(-50%)';
    errorEl.style.zIndex = '9999';
    errorEl.style.padding = '10px 20px';
    errorEl.style.borderRadius = '4px';
    errorEl.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
    errorEl.style.maxWidth = '400px';
    errorEl.style.width = 'auto';
    errorEl.innerHTML = `<i class="fas fa-exclamation-circle me-2"></i>${message}`;
    
    // 添加到页面
    document.body.appendChild(errorEl);
    
    // 3秒后自动消失
    setTimeout(() => {
        errorEl.style.opacity = '0';
        errorEl.style.transition = 'opacity 0.5s ease';
        
        setTimeout(() => {
            if (errorEl.parentNode) {
                errorEl.parentNode.removeChild(errorEl);
            }
        }, 500);
    }, 3000);
}

/**
 * 检测当前设备类型
 * @returns {Object} 设备类型信息
 */
function detectDevice() {
    const ua = navigator.userAgent.toLowerCase();
    const isIOS = /iphone|ipad|ipod/.test(ua);
    const isAndroid = /android/.test(ua);
    const isWechat = /micromessenger/.test(ua);
    const isMobile = isIOS || isAndroid || /mobile/.test(ua);
    
    return {
        isIOS,
        isAndroid,
        isWechat,
        isMobile
    };
}

/**
 * 打开导航下拉菜单 (多地图支持)
 * @param {object} event - 事件对象 
 * @param {string} name - 地点名称
 * @param {string} address - 地址信息
 * @param {string} lat - 纬度 (可选)
 * @param {string} lng - 经度 (可选)
 */
function openMapNavigation(event, name, address, lat, lng) {
    // 参数验证
    if (!name) {
        console.error('导航功能错误: 未提供地点名称');
        showNavigationError('导航信息不完整，请提供地点名称');
        return;
    }
    
    // 阻止默认事件
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    
    // 获取设备信息
    const device = detectDevice();
    
    // 创建不同地图服务的导航项
    const navItems = [];
    
    // 百度地图（通用）
    navItems.push({
        name: '百度地图',
        icon: 'fa-map-marked-alt',
        color: '#3385ff',
        action: () => navigateBaiduMap(lat, lng, name, address)
    });
    
    // 高德地图（通用）
    navItems.push({
        name: '高德地图',
        icon: 'fa-map-marked-alt',
        color: '#00b2a9',
        action: () => navigateAMap(lat, lng, name, address)
    });
    
    // 腾讯地图（通用）
    navItems.push({
        name: '腾讯地图',
        icon: 'fa-map-marked-alt',
        color: '#3cbd41',
        action: () => navigateTencentMap(lat, lng, name, address)
    });
    
    // 根据设备添加更多选项
    if (device.isIOS) {
        // iOS设备添加Apple地图
        navItems.push({
            name: 'Apple地图',
            icon: 'fa-apple',
            color: '#999',
            action: () => navigateAppleMap(lat, lng, name, address)
        });
    }
    
    // 添加Google地图（通用但可能被墙）
    navItems.push({
        name: 'Google地图',
        icon: 'fa-map-marked-alt',
        color: '#4285f4',
        action: () => navigateGoogleMap(lat, lng, name, address)
    });
    
    // 移除之前的下拉菜单
    if (activeMapDropdown) {
        activeMapDropdown.remove();
        activeMapDropdown = null;
    }
    
    // 创建下拉菜单HTML
    const dropdownContent = navItems.map(item => `
        <a href="javascript:void(0);" class="map-nav-item" style="color: ${item.color};">
            <i class="fas ${item.icon}"></i> ${item.name}
        </a>
    `).join('');
    
    const dropdownTitle = `<div class="map-dropdown-title">导航到: ${name}</div>`;
    
    const dropdownHtml = `
    <div class="map-dropdown">
        ${dropdownTitle}
        <div class="map-dropdown-content">
            ${dropdownContent}
        </div>
    </div>`;
    
    // 添加新的下拉菜单
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = dropdownHtml;
    const dropdown = tempDiv.firstElementChild;
    document.body.appendChild(dropdown);
    
    // 定位下拉菜单
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;
    
    // 优化移动端位置
    if (device.isMobile) {
        dropdown.style.position = 'fixed';
        dropdown.style.bottom = '20px';
        dropdown.style.left = '50%';
        dropdown.style.transform = 'translateX(-50%)';
        dropdown.style.width = 'calc(100% - 40px)';
        dropdown.style.maxWidth = '400px';
    } else if (event) {
        // 桌面设备根据点击位置显示
        dropdown.style.position = 'absolute';
        
        const rect = dropdown.getBoundingClientRect();
        let top = (event.clientY + window.scrollY);
        let left = (event.clientX + window.scrollX);
        
        // 确保下拉菜单不会超出视口
        if (left + rect.width > viewportWidth) {
            left = viewportWidth - rect.width - 10;
        }
        
        if (top + rect.height > viewportHeight + window.scrollY) {
            top = top - rect.height - 10;
        }
        
        dropdown.style.top = top + 'px';
        dropdown.style.left = left + 'px';
    }
    
    // 保存当前下拉菜单引用
    activeMapDropdown = dropdown;
    
    // 为下拉菜单中的项添加点击事件
    const navLinks = dropdown.querySelectorAll('.map-nav-item');
    navLinks.forEach((link, index) => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // 执行对应的导航动作
            navItems[index].action();
            
            // 关闭下拉菜单
            dropdown.remove();
            activeMapDropdown = null;
        });
    });
    
    // 添加样式
    addDropdownStyles();
}

/**
 * 添加下拉菜单样式
 */
function addDropdownStyles() {
    // 检查是否已添加样式
    if (document.getElementById('map-dropdown-styles')) {
        return;
    }
    
    // 创建样式元素
    const styleEl = document.createElement('style');
    styleEl.id = 'map-dropdown-styles';
    
    // 添加样式规则
    styleEl.textContent = `
        .map-dropdown {
            position: fixed;
            z-index: 9999;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            border-radius: 8px;
            overflow: hidden;
            min-width: 200px;
            animation: fadeIn 0.2s ease;
        }
        
        .map-dropdown-title {
            padding: 12px 15px;
            background: #f8f9fa;
            border-bottom: 1px solid #eee;
            font-weight: bold;
            color: #333;
        }
        
        .map-dropdown-content {
            display: flex;
            flex-direction: column;
            max-height: 300px;
            overflow-y: auto;
        }
        
        .map-dropdown-content a {
            padding: 12px 15px;
            text-decoration: none;
            transition: background-color 0.3s;
            display: flex;
            align-items: center;
        }
        
        .map-dropdown-content a:hover {
            background-color: #f5f5f5;
        }
        
        .map-dropdown-content i {
            margin-right: 10px;
            width: 20px;
            text-align: center;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @media (max-width: 768px) {
            .map-dropdown {
                border-radius: 12px;
            }
            
            .map-dropdown-content a {
                padding: 15px;
                font-size: 16px;
            }
        }
    `;
    
    // 添加到文档头部
    document.head.appendChild(styleEl);
} 