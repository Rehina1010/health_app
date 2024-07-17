from .models import User

async def save_user(data):
    print('Start save')
    if not await is_user_exist(chat_id=data['chat_id']):
        user = User(first_name=data['first_name'], last_name=data['last_name'], language=data['language'],
                    chat_id=data['chat_id'])
        user.save()
        print('Save successfully')
    else:
        print('User already exist')
        await change_user_status(chat_id=data['chat_id'], status=True)



async def is_user_exist(chat_id) -> bool:
   user = User.objects(chat_id=chat_id).first()
   if user:
       return True
   else:
       return False



async def get_all_users() -> list[User]:
    users = User.objects(is_active=True).all()
    return users

async  def change_user_status(chat_id: int, status: bool):
    user = User.objects(chat_id=chat_id).first()
    user.is_active = status
    user.save()
