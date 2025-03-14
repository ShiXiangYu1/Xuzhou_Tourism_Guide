/**
 * 徐州旅游攻略网站的主要JavaScript文件
 * 提供页面交互增强功能
 */

// 等待DOM完全加载
document.addEventListener('DOMContentLoaded', function() {
    // 初始化所有功能
    highlightCurrentNav();
    setupSmoothScroll();
    lazyLoadImages();
    setupDropdownClosers();
});

/**
 * 高亮当前页面在导航菜单中的对应项
 */
function highlightCurrentNav() {
    // 获取当前页面路径
    const currentPath = window.location.pathname;
    
    // 获取所有导航链接
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    // 为匹配当前路径的链接添加active类
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || 
            (currentPath !== '/' && href !== '/' && currentPath.includes(href))) {
            link.classList.add('active');
        }
    });
}

/**
 * 设置平滑滚动到锚点
 */
function setupSmoothScroll() {
    // 获取所有锚点链接
    const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
    
    // 为每个锚点链接添加点击事件
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // 获取目标元素
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            // 如果目标元素存在，则平滑滚动到该位置
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * 设置图片懒加载
 */
function lazyLoadImages() {
    // 如果浏览器支持IntersectionObserver，则使用它进行懒加载
    if ('IntersectionObserver' in window) {
        // 获取所有带有data-src属性的图片
        const lazyImages = document.querySelectorAll('img[data-src]');
        
        // 创建观察器配置
        const options = {
            rootMargin: '0px 0px 50px 0px',
            threshold: 0.1
        };
        
        // 创建观察器实例
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    const src = img.getAttribute('data-src');
                    
                    if (src) {
                        img.src = src;
                        img.removeAttribute('data-src');
                    }
                    
                    // 图片加载后停止观察
                    observer.unobserve(img);
                }
            });
        }, options);
        
        // 为每个懒加载图片添加观察
        lazyImages.forEach(img => {
            observer.observe(img);
        });
    } else {
        // 如果浏览器不支持IntersectionObserver，则使用滚动事件进行懒加载
        let lazyImageTimeout;
        
        function lazyLoadImagesOnScroll() {
            if (lazyImageTimeout) {
                clearTimeout(lazyImageTimeout);
            }
            
            lazyImageTimeout = setTimeout(function() {
                const lazyImages = document.querySelectorAll('img[data-src]');
                const scrollTop = window.pageYOffset;
                
                lazyImages.forEach(img => {
                    if (img.offsetTop < (window.innerHeight + scrollTop)) {
                        const src = img.getAttribute('data-src');
                        
                        if (src) {
                            img.src = src;
                            img.removeAttribute('data-src');
                        }
                    }
                });
                
                // 如果所有图片都已加载，则移除滚动事件监听器
                if (document.querySelectorAll('img[data-src]').length === 0) {
                    document.removeEventListener('scroll', lazyLoadImagesOnScroll);
                    window.removeEventListener('resize', lazyLoadImagesOnScroll);
                    window.removeEventListener('orientationChange', lazyLoadImagesOnScroll);
                }
            }, 20);
        }
        
        // 添加滚动事件监听器
        document.addEventListener('scroll', lazyLoadImagesOnScroll);
        window.addEventListener('resize', lazyLoadImagesOnScroll);
        window.addEventListener('orientationChange', lazyLoadImagesOnScroll);
        
        // 初始调用一次
        lazyLoadImagesOnScroll();
    }
}

/**
 * 设置所有下拉菜单的自动关闭
 */
function setupDropdownClosers() {
    // 获取所有下拉菜单
    const dropdowns = document.querySelectorAll('.dropdown');
    
    // 点击页面任意位置关闭已打开的下拉菜单
    document.addEventListener('click', function(e) {
        const openDropdowns = document.querySelectorAll('.dropdown-menu.show');
        openDropdowns.forEach(dropdown => {
            // 如果点击位置不在当前下拉菜单内，则关闭它
            if (!dropdown.contains(e.target) && !dropdown.previousElementSibling.contains(e.target)) {
                dropdown.classList.remove('show');
            }
        });
    });
}

/**
 * 路由变化监听
 * 用于SPA应用中监听路由变化并触发相应操作
 * 修复MutationObserver错误
 */
function watchRouteChange(callback) {
    // 检查是否有合适的DOM节点来观察
    const targetNode = document.querySelector('body');
    
    // 如果没有找到合适的DOM节点，则返回
    if (!targetNode) {
        console.warn('未找到可观察的DOM节点，路由变化监听未启动');
        return;
    }
    
    // 观察配置
    const config = { 
        attributes: false, 
        childList: true, 
        subtree: true 
    };
    
    // 创建观察器实例
    const observer = new MutationObserver((mutationsList) => {
        for (const mutation of mutationsList) {
            if (mutation.type === 'childList') {
                // 路由变化后可能会添加/移除节点，触发回调
                if (typeof callback === 'function') {
                    callback();
                }
                break;
            }
        }
    });
    
    // 开始观察
    try {
        observer.observe(targetNode, config);
    } catch (error) {
        console.error('路由变化监听启动失败：', error);
    }
    
    // 返回观察器实例，以便在需要时停止观察
    return observer;
} 