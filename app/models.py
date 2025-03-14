#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
数据模型模块
定义网站所需的数据结构和数据
"""


class FoodItem:
    """美食项目类，表示一个美食推荐"""
    
    def __init__(self, name, category, location, description, rating, image=None):
        """
        初始化美食项目
        
        Args:
            name: 美食名称
            category: 美食类别（如烧烤、小吃等）
            location: 地点位置
            description: 详细描述
            rating: 评分（1-5）
            image: 图片路径
        """
        self.name = name
        self.category = category
        self.location = location
        self.description = description
        self.rating = rating
        self.image = image or "default_food.jpg"
    
    def to_dict(self):
        """
        将对象转换为字典
        
        Returns:
            dict: 包含对象属性的字典
        """
        return {
            'name': self.name,
            'category': self.category,
            'location': self.location,
            'description': self.description,
            'rating': self.rating,
            'image': self.image
        }


class Attraction:
    """景点类，表示一个景点推荐"""
    
    def __init__(self, name, category, address, description, rating, 
                 opening_hours=None, ticket_price=None, image=None):
        """
        初始化景点
        
        Args:
            name: 景点名称
            category: 景点类别（如历史文化、自然景观等）
            address: 详细地址
            description: 详细描述
            rating: 评分（1-5）
            opening_hours: 开放时间
            ticket_price: 门票价格
            image: 图片路径
        """
        self.name = name
        self.category = category
        self.address = address
        self.description = description
        self.rating = rating
        self.opening_hours = opening_hours
        self.ticket_price = ticket_price
        self.image = image or "default_attraction.jpg"
    
    def to_dict(self):
        """
        将对象转换为字典
        
        Returns:
            dict: 包含对象属性的字典
        """
        return {
            'name': self.name,
            'category': self.category,
            'address': self.address,
            'description': self.description,
            'rating': self.rating,
            'opening_hours': self.opening_hours,
            'ticket_price': self.ticket_price,
            'image': self.image
        }


class Itinerary:
    """行程计划类，表示一天的行程安排"""
    
    def __init__(self, day, morning_plan, lunch_plan, afternoon_plan, dinner_plan):
        """
        初始化行程计划
        
        Args:
            day: 第几天
            morning_plan: 上午计划
            lunch_plan: 午餐计划
            afternoon_plan: 下午计划
            dinner_plan: 晚餐计划
        """
        self.day = day
        self.morning_plan = morning_plan
        self.lunch_plan = lunch_plan
        self.afternoon_plan = afternoon_plan
        self.dinner_plan = dinner_plan
    
    def to_dict(self):
        """
        将对象转换为字典
        
        Returns:
            dict: 包含对象属性的字典
        """
        return {
            'day': self.day,
            'morning_plan': self.morning_plan,
            'lunch_plan': self.lunch_plan,
            'afternoon_plan': self.afternoon_plan,
            'dinner_plan': self.dinner_plan
        }


# 预定义的美食数据
FOOD_DATA = [
    FoodItem(
        "老玖烧烤（九路烧烤）", 
        "烧烤", 
        "和平路", 
        "徐州最知名的烧烤品牌之一，以羊肉串和特色腌制技术闻名，推荐尝试羊排和鸡翅",
        5.0, 
        "laojiushaokao.jpg"
    ),
    FoodItem(
        "火筷子烧烤", 
        "烧烤", 
        "万达广场附近", 
        "环境较好，特色是调料独特，肉质鲜嫩",
        4.5, 
        "huokuaizi.jpg"
    ),
    FoodItem(
        "大铁棍儿烧烤", 
        "烧烤", 
        "云龙区大龙湖附近", 
        "民间风味浓厚，特色是铁棍烤制，使食材保持原汁原味",
        4.8, 
        "datiegun.jpg"
    ),
    FoodItem(
        "奇火烧烤", 
        "烧烤", 
        "淮海西路", 
        "有名的深夜食堂，尤其推荐烤生蚝和烤羊肉",
        4.7, 
        "qihuo.jpg"
    ),
    FoodItem(
        "徐州烙馍", 
        "特色小吃", 
        "市中心多处小吃街", 
        "当地特色面食，外脆里软",
        4.5, 
        "laomo.jpg"
    ),
    FoodItem(
        "香辣鸡架", 
        "特色小吃", 
        "小吃街", 
        "徐州特色卤味，入味且香辣",
        4.3, 
        "jijia.jpg"
    ),
    FoodItem(
        "彭城汤包", 
        "特色小吃", 
        "市区多家连锁店", 
        "徐州名小吃，皮薄馅多，汤汁丰盈",
        4.6, 
        "tangbao.jpg"
    ),
    FoodItem(
        "小鱼卷饼", 
        "特色小吃", 
        "中山北路凉皮店旁", 
        "不起眼的小店，但卷饼外酥里嫩，小鱼鲜香可口，排队人很多，值得一等",
        4.9, 
        "xiaoyujuanbing.jpg"
    ),
    FoodItem(
        "老王地锅", 
        "特色菜", 
        "云龙区新农贸市场附近", 
        "朴实无华的店面，地锅菜香味浓郁，食材新鲜，是当地人常去的美食地点",
        4.7, 
        "laowangdiguo.jpg"
    ),
    FoodItem(
        "徐州凉皮", 
        "特色小吃", 
        "中山北路小吃街", 
        "劲道爽滑，调料香辣，夏季必备开胃小吃，往里走可以看到排队购买的人群",
        4.8, 
        "liangpi.jpg"
    )
]

# 预定义的景点数据
ATTRACTION_DATA = [
    Attraction(
        "云龙山风景区", 
        "历史文化类", 
        "徐州市云龙区云龙山", 
        "徐州地标，可俯瞰全城",
        4.8, 
        "08:00-18:00", 
        "60元", 
        "yunlongshan.jpg"
    ),
    Attraction(
        "汉文化景区", 
        "历史文化类", 
        "徐州市铜山区", 
        "包括汉兵马俑、汉画像石馆等",
        4.7, 
        "09:00-17:00", 
        "80元", 
        "hanwenhua.jpg"
    ),
    Attraction(
        "楚王陵", 
        "历史文化类", 
        "徐州市铜山区", 
        "西楚霸王项羽的陵墓",
        4.6, 
        "08:30-17:30", 
        "40元", 
        "chuwangling.jpg"
    ),
    Attraction(
        "徐州博物馆", 
        "历史文化类", 
        "徐州市云龙区东段", 
        "了解徐州深厚的历史文化",
        4.9, 
        "09:00-17:00", 
        "免费", 
        "museum.jpg"
    ),
    Attraction(
        "云龙湖", 
        "自然景观类", 
        "徐州市云龙区", 
        "市中心最大湖泊，适合散步休闲",
        4.7, 
        "全天开放", 
        "免费", 
        "yunlonghu.jpg"
    ),
    Attraction(
        "潘安湖湿地公园", 
        "自然景观类", 
        "徐州市贾汪区", 
        "生态环境优美，适合亲近自然",
        4.5, 
        "08:00-17:30", 
        "30元", 
        "pananhu.jpg"
    )
]

# 预定义的行程数据
ITINERARY_DATA = [
    Itinerary(
        1,
        "参观徐州博物馆，了解徐州历史文化",
        "在附近品尝徐州烙馍和彭城汤包",
        "游览汉文化景区，参观汉兵马俑",
        "晚上去老玖烧烤体验正宗徐州烧烤"
    ),
    Itinerary(
        2,
        "登云龙山，俯瞰徐州全城",
        "在山上餐厅享用午餐",
        "游览云龙湖，欣赏湖光山色",
        "晚上去火筷子烧烤，品尝特色烤生蚝"
    ),
    Itinerary(
        3,
        "游览潘安湖湿地公园",
        "前往苏园饭店品尝地方菜",
        "万达广场购物休闲",
        "逍遥津附近觅食，品尝各种小吃"
    )
]

# 预定义的实用信息数据
PRACTICAL_INFO = {
    "transportation": {
        "external": "徐州有高铁站和机场，交通便利",
        "internal": "公交系统发达，也可使用打车软件",
        "recommendation": "在市中心租借共享单车游览市区景点"
    },
    "accommodation": {
        "high_end": ["徐州金鹰尊荣酒店", "徐州万达希尔顿酒店"],
        "mid_range": ["如家酒店", "徐州锦江之星"],
        "special": "云龙山下有部分民宿，环境优美"
    },
    "season": {
        "best_time": "4-5月和9-10月，气候宜人",
        "bbq_season": "全年均可，夏季夜晚户外烧烤别有风味"
    },
    "tips": [
        "徐州夏季较热，请做好防晒准备",
        "品尝特色美食时注意卫生和个人口味偏好",
        "景点游览建议提前查询开放时间",
        "徐州话有特色，可学几句当地方言增添旅行乐趣"
    ]
} 