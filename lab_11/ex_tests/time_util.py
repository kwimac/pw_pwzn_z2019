from datetime import datetime

def tell_me_yesterday():
    print(f'Yesterday was: {datetime.now().strftime("%Y-%m-%d")}')
