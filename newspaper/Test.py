LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'style': '{',
    # Настройка форматтеров
    'formatters': {
        'debugformatter': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warningformatter': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },
        'errorformatter': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(exc_info)s %(message)s'
        },
        'generalfileformatter': {
            'format': '%(asctime)s %(module)s %(message)s'
        },
        'errorfileformatter': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(exc_info)s'
        },
        'securityfileformatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'sendmailadmins': {
            'format': '%(asctime)s %(levelname)s %(pathname)s'
        },
    },
    # Настройка фильтров
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    # Настройка хендлерров с указанием форматтеров, уровней и фильтров
    'handlers': {
        'console1': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debugformatter',
        },
        'console2': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warningformatter',
        },
        'console3': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'errorformatter',
        },
        'filegeneral': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'generalfileformatter',
        },
        'fileerrors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'errorfileformatter'
        },
        'filesecurity': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'securityfileformatter'
        },
        'mailadmins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'sendmailadmins'
        },
    },
    # Настройка логгеров с указанием используемого хендлера
    'loggers': {
        'django': {
            'handlers': ['console1', 'console2', 'console3', 'filegeneral'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['fileerrors', 'mailadmins'],
            'propagate': True,
        },
        'django.server': {
            'handlers': ['fileerrors', 'mailadmins'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['fileerrors'],
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['fileerrors'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['filesecurity'],
            'propagate': True,
        },
    },
},
