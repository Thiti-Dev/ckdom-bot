bot_configs = {
    "collecting_data": {
        "sugar":{
            "img_name": "sugar_area.png",
            "confidence": 0.975
        },
        "jelly":{
            "img_name": "jelly_area.png",
            "confidence": 0.965            
        },
        "smith":{
            "img_name": "smith_area.png",
            "confidence": 0.96            
        },
        "lumberjack":{
            "img_name": "lumberjack_area.png",
            "confidence": 0.97
        },
        "jammery":{
            "img_name": "jammery_area.png",
            "confidence": 0.97
        },
        "jellystar":{
            "img_name": "jellystart_area.png",
            "confidence": 0.84,
            "chained": True # if chained -> no need to iterate other element
        },
        "carpentry":{
            "img_name": "carpentry_area.png",
            "confidence": 0.97,
            "additional": {
                "x": 100,
                "y": 0
            }
        }
    }
}