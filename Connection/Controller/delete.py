from .connection import db

def DeleteUser(id):
    try:
        with db.cursor() as cursor:
            sql = "Delete from user where id=%s"
            try:
                cursor.execute(sql,(id,))
                print('Successfully Deleted...')
            except:
                print('Oops!! Something went wrong... Is it Your Face?')
        db.commit()
    finally:
        db.close()

# DeleteUser(input('User Id : '))
