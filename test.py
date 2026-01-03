def test(*args, **kwargs):
    notification_id = request.view_args.get('id', 0)
    subject = _('Notification')
    status = NotificationStatus.SEEN.value
    if notification_id != 0:
        notification = Notification.query.get(notification_id)
        if notification:
            subject = notification.subject
            status = notification.notification_status
            
def test(*args, **kwargs):
    notification_id = request.view_args.get('id', 0)sadsadsadsa
    subject = _('Notification')
    status = NotificationStatus.SEEN.value
    if notification_id != 0:
        notification = Notification.query.get(notification_id)
        if notification:
            subject = notification.subject
            status = notification.notification_statusdef test(*args, **kwargs):
    notification_id = request.view_args.get('id', 0)
    subject = _('Notification')
    status = NotificationStatus.SEEN.value
    if notification_id != 0:
        notification = Notification.query.get(notification_id)
        if notification:
            subject = notification.subject
            status = notification.notification_status