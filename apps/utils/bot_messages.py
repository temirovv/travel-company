# message for advertising for telegram channels
msg_channel = '''
{}
'''


# message for admin when user book any package
def make_msg_admin(
        phone, package_name, amount,
        order_id, transaction_check, booked_date,
        message, package_detail):
    """

    :param phone: Telefon raqam
    :param package_name: Paket nomi
    :param amount: To'langan summa
    :param order_id: Zakaz Aydisi
    :param transaction_check: Tranzaksiya tavsilotlari
    :param booked_date: Bron qilingan sana
    :param message: Mijoz qoldirgan xabar
    :param package_detail: Xarid qilingan Paket xavolasi
    :return: str
    """

    msg_admin = '''
    Yangi bron amalga oshirildi
    
    telefon raqami:     {0}
    paket nomi:         {1}
    to'langan summa:    {2}
    zakas id si:        {3}
    <a href="{4}">To'lov cheki</a>
    bron qilish sanasi: {5}
    
    Mijoz qoldirgan xabar:
    {6}
    
    
    <a href="{7}">xarid qilingan paketning qo'shimcha detallari uchun</a>
    '''
    return msg_admin.format(
        phone, package_name, amount, order_id,
        transaction_check, booked_date, message, package_detail
    )


def make_package_detail_msg(text: str, **kwargs):
    if kwargs:
        images = kwargs.get('images')
        videos = kwargs.get('videos')



    f"""
    
    """
