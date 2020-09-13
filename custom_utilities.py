import os
import shutil
import argparse

def deleteMigrations(folder_path,dir_space=0):
    if os.path.isdir(folder_path):
        if os.path.basename(folder_path) == 'migrations':
            print(' |   '*dir_space,'├──',folder_path," >> Deleted") #└──
            shutil.rmtree(folder_path)
        else:
            next_path = os.listdir(folder_path)
            for i,path in enumerate(next_path):
                next_path[i] = os.path.join(folder_path,path)
            for i,further_path in enumerate(next_path):
                deleteMigrations(further_path,(dir_space+1))

def makeMigrations():
    s = os.popen('python manage.py makemigrations axisUsers')
    o = s.read()
    print(o)
    s = os.popen('python manage.py makemigrations axisPosts')
    o = s.read()
    print(o)
    s = os.popen('python manage.py makemigrations axisPMS')
    o = s.read()
    print(o)

def migrateAll():
    s = os.popen('python manage.py migrate')
    o = s.read()
    print(o)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    p = argparse.ArgumentParser()
    p.add_argument('--delMigrations',action='store_true', help='Delete All Migration Folders')
    p.add_argument('--makemigrations',action='store_true', help='Make Migrations for all Apps')
    p.add_argument('--migrate',action='store_true', help='Migrate with manage.py')
    args = p.parse_args()
    if args.delMigrations:
        print("Deleting all migration folders from all Apps ...\n")
        deleteMigrations(dir_path)
        print("## Done.")
    if args.makemigrations:
        print("Creating new migrations on all Apps ...\n")
        makeMigrations()
        print("## Done.")
    if args.migrate:
        print("Applying all new migrations on all Apps ...\n")
        migrateAll()
        print("## Done.")