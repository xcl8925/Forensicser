class AppInfo:
    # 编号，uid，应用名称，主控地址，创建时间，到期时间，分发链接，
    def __init__(self, app_id='', uid='', name='', domain='', create_time='', end_time='', delivery=''):
        self.app_id = app_id
        self.uid = uid
        self.name = name
        self.domain = domain
        self.create_time = create_time
        self.end_time = end_time
        self.delivery = delivery

    def as_dict(self):
        return {'app_id': self.app_id, 'uid': self.uid, 'name': self.name, 'domain': self.domain,
                'create_time': self.create_time, 'end_time': self.end_time, 'delivery': self.delivery}

    def __str__(self):
        return self.as_dict().__str__()


class UserInfo:
    def __init__(self, uid='', user_name='', count='', login_ip='', last_login_time='', register_time=''):
        self.uid = uid
        self.user_name = user_name
        self.count = count
        self.login_ip = login_ip
        self.last_login_time = last_login_time
        self.register_time = register_time

    def as_dict(self):
        return {'uid': self.uid, 'user_name': self.user_name, 'count': self.count, 'login_ip': self.login_ip,
                'last_login_time': self.last_login_time, 'register_time': self.register_time}

    def __str__(self):
        return self.as_dict().__str__()


class AppUserInfo:
    def __init__(self, app_info=None, user_info=None):
        self.app_info = app_info
        self.user_info = user_info

    def as_dict(self):
        return {'app_id': self.app_info.app_id if self.app_info is not None else '',
                'uid': self.app_info.uid if self.app_info is not None else '',
                'name': self.app_info.name if self.app_info is not None else '',
                'domain': self.app_info.domain if self.app_info is not None else '',
                'create_time': self.app_info.create_time if self.app_info is not None else '',
                'end_time': self.app_info.end_time if self.app_info is not None else '',
                'delivery': self.app_info.delivery if self.app_info is not None else '',
                'user_name': self.user_info.user_name if self.user_info is not None else '',
                'count': self.user_info.count if self.user_info is not None else '',
                'login_ip': self.user_info.login_ip if self.user_info is not None else '',
                'last_login_time': self.user_info.last_login_time if self.user_info is not None else '',
                'register_time': self.user_info.register_time if self.user_info is not None else ''}


class UserVerifyInfo:
    def __init__(self, uid='', real_name='', location='', id_card='', front='', back='', handle='', ):
        self.uid = uid
        self.real_name = real_name
        self.location = location
        self.id_card = id_card
        self.front = front
        self.back = back
        self.handle = handle

    def as_dict(self):
        return {'uid': self.uid, 'real_name': self.real_name, 'location': self.location, 'id_card': self.id_card,
                'front': self.front, 'back': self.back, 'handle': self.handle}

    def __str__(self):
        return self.as_dict().__str__()
