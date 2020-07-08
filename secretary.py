documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }
      
def welcome():
  print(" __          __  _                          _ \n \ \        / / | |                        | |\n  \ \  /\  / /__| | ___ ___  _ __ ___   ___| |\n   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |\n    \  /\  /  __/ | (_| (_) | | | | | |  __/_|\n     \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)")
  print()
  print("Добро пожаловать в нашу интерактивную систему документооборота!")
  main()

def help_func():
  print("", "'p' – узнать имя владельца документа",
  "'l' – вывести список всех документов",
  "'s' – узнать номер полки, на которой находится документ",
  "'a' – добавить новый документ",
  "'d' – удалить документ",
  "'m' – переместить документ",
  "'as' – добавить новую полку",
  "'sa' – вывести список всех полок",
  "'do' – вывести список имен всех владельцев документов",
  "'q' - выход", "", sep = '\n')
  user_input = input("Хотите выйти из режима справки? да/нет: ")
  if user_input == 'да':
    main()

def search_doc_number(doc_number):
  names = []
  for docs in documents:
    if docs['number'] == doc_number:
      names.append(docs['name'])
  return len(names)

def check_shelf(shelf_number):
  if shelf_number not in directories.keys():
      print('\nПолка с таким номером не существует.')
      if input("Хотите создать полку с таким номером? да/нет ") == 'да':
        add_shelf(shelf_number)
      else:
        print("\nКоманда не может быть выполнена, так как полка с таким номером не существует.")

def another_com():
  if input("\nХотите выполнить другую команду? да/нет ") == 'да':
    main()
  else:
    print('До свидания!')

def people(doc_number):
  if search_doc_number(doc_number) == 0:
      print('\nДокумент с данным номером не найден')
  else:
    for docs in documents:
      if docs['number'] == doc_number:
        return docs['name']

def list_func():
  print('\nСписок доступных документов:\n')
  for docs in documents:
    print('- ' + docs['type'], '"' + docs['number'] + '"', '"'+ docs['name'] + '"',)

def shelf(doc_number):
  if search_doc_number(doc_number) == 0:
    print('\nДокумент с данным номером не найден')
  else:
    for shelves, lists in directories.items():
      if doc_number in lists:
        print(f'\nДанный документ находится на полке  №{shelves}')

def add(doc_number):
  if search_doc_number(doc_number) == 0:
    new_doc = {}
    new_doc['type'] = input('Введите тип документа: ')
    
    new_doc['name'] = input('Введите имя владельца: ')
    shelf_number = input('Введите номер полки: ')
    new_doc['number'] = doc_number
    check_shelf(shelf_number)
    if shelf_number in directories.keys():
      documents.append(new_doc)
      directories[shelf_number].append(doc_number)
      print('\nДокумент успешно добавлен')
  else:
      print('Документ с таким номером уже существует')

def delete(doc_number):
  if search_doc_number(doc_number) ==0:
    print('\nДокумент с данным номером не найден')
  else:
    for lists in directories.values():
      if doc_number in lists:
        lists.remove(doc_number)
    for docs in range(len(documents)):
      if documents[docs].get('number') == doc_number:
        del documents[docs]
        break
    print('\nДокумент успешно удален')
      
def move(doc_number):
  if search_doc_number(doc_number) == 0:
    print('\nДокумент с данным номером не найден')
  else:
    shelf_number = input('На какую полку переместить документ? ')
    check_shelf(shelf_number)
    if shelf_number in directories.keys():
      for lists in directories.values():
        if doc_number in lists:
          lists.remove(doc_number)
          directories[shelf_number].append(doc_number)
      print('\nДокумент успешно перемещен')

def add_shelf(shelf_number):
  if shelf_number in directories.keys():
      print('\nПолка с таким номером уже существует')
  else:
    directories[shelf_number] = []
    print('\nПолка успешна добавлена')

def show_all():
  print('\nСписок доступных полок:\n')
  for shelves, docs in directories.items():
    print(f'- Полка №{shelves}, на которой хранятся документы:{docs}')

def document_owners():
    for docs in documents:
        try:
            print(docs['name'])
        except KeyError:
            print('Отсутствует имя владельца документа')
        

def main():
  while True:
    command = input('\nВведите команду, либо вызовите справку по доступным опциям с помощью команды "help": ')
    if command == 'help':
      help_func()
    elif command == 'p':
      doc_number = input('Введите номер документа: ')
      people(doc_number)
      another_com()
    elif command == 'l':
      list_func()
      another_com()
    elif command == 's':
      doc_number = input('Введите номер документа: ')
      shelf(doc_number)
      another_com()
    elif command == 'a':
      doc_number = input('Введите номер документа: ')
      add(doc_number)
      another_com()
    elif command == 'd':
      doc_number = input('Введите номер документа: ')
      delete(doc_number)
      another_com()
    elif command == 'm':
      doc_number = input('Введите номер документа: ')
      move(doc_number)
      another_com()
    elif command == 'as':
      shelf_number = input('Введите номер полки: ')
      add_shelf(shelf_number)
      another_com()
    elif command == 'sa':
      show_all()
      another_com()
    elif command == 'do':
      document_owners()
      another_com()
    elif command == 'q':
      print('До свидания!')  
    else:
      print('Команда введена неверно. Ознакомьтесь со списком допустимых команд.')
      help_func()
    break

# welcome()
main()

