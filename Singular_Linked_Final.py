import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    # Inserting element at begining of LL
    def push(self,ll,  value):
        if ll.head ==None:
            print('LL is empty')
            return
        else:
            ll.Traversal()
            new_node = Node(value)
            new_node.next = ll.head
            ll.head = new_node
            #ll.Traversal()
            return ll

    # INserting element at the end of LL
    def append(self,ll, value):
        if ll.head is None:
            return print('LL is empty')
        else:
            ll.Traversal()
            temp = ll.head
            while temp.next:
                temp = temp.next

            new_node = Node(value)
            temp.next = new_node
            return ll

    # Inserting element in after of nodes
    def Inserting_inbetween(self, ll,  pre_value, value):
        ll.Traversal()
        print('previous node value', pre_value)
        temp = ll.head
        new_node = Node(value)

        if ll.head is None:
            return print('Empty LL')
        while temp:
            if pre_value == temp.data:
                new_node.next = temp.next
                temp.next = new_node
            temp = temp.next
        return ll


    ##Linked list TRaversal
    def Traversal(self):
        if self.head is None:
            return print('LL is empty')

        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


    def delete_by_index(self, ll, index):
        print('Index to be deleted: {}'.format(index))
        temp = ll.head
        if temp is None:
            return print('Empty LL')

        c = 0
        prev = None
        while temp:
            if index == c:
                if index==0:
                    next = temp.next
                    ll.head = next
                    #print(ll.head.data)

                    return  ll
                prev.next = temp.next
            c += 1
            prev = temp
            temp = temp.next
        return ll

    # DEleting a node by its value not by index
    def delete_by_value(self, ll, value):
        temp = ll.head
        print(temp.data)
        if temp is None:
            return print('Linked list is empty')

        elif temp.data == value:
            print('Value to be deleted is head :', temp.data)
            temp = temp.next
            ll.head = temp
            ll.Traversal()
            return ll
        else:
            prev = Node(None)
            while temp:
                if temp.data == value:
                    prev.next = temp.next
                    return ll
                prev = temp
                temp = temp.next
            return ll

    # Fetching Nth NOde FRom LL
    def Nth_Node_LL(self, ll,  N):
        temp = ll.head
        if temp is None:
            return print('Empty LL')
        #Counter to fetch Nth index
        c = 0
        while temp:
            if c == N:
                print(temp.data)
                return temp.data
            temp = temp.next
            c += 1

    ##DEleting whole LInked list
    def delete_ll(self) -> None:
        if self.head is None:
            return print('LL is already EMPTY')
        self.head = None
        return print('DEleted whole LL')




class trigger:
    FLAG = True

    while FLAG:

        print("""1:Create New LL  2:Delete LL 3:Add Node  4:Delete Node  5:Traverse LL  7:Fetching Nth NOde  6:Exit Program""")
        try:
            option = int(input('Enter any of the above options: '))
            if option == 1:
                ll = Linked_list()
                ll.head = Node(int(input('Add Head Value')))
                ll.Traversal()

            elif option == 2:
                print('In delete ll', ll.head.data)
                ll.delete_ll()

            elif option == 3:
                flag = True
                ll.Traversal()
                #print(ll.head.data)
                while flag:
                    insert = (int(input("""select below option to add new node in ll
                    1:at the begining
                    2:at the end
                    3:after given node""")))
                    if insert == 1:
                        Llist = ll.push(ll, int(input('Node to insert at begining')))
                        print('After Node addition:')
                        Llist.Traversal()

                    elif insert == 2:
                        Llist = ll.append(ll, int(input('Node to insert at end')))
                        print('After Node addition:')
                        Llist.Traversal()

                    elif insert == 3:
                        print('work in progress')
                        select = int(input('1:Index 2:Value '))
                        if select == 1:
                            index = int(input('enter Index after which New node is added'))
                            value = ll.Nth_Node_LL(ll,index)
                            print('{} is available at {} index'.format(value, index))
                            Llist = ll.Inserting_inbetween(ll, value,
                                                          int(input('Node to insert after given node')))
                        if select ==2:
                            ll.Traversal()
                            value = int(input('Enter value in LL after new node is added'))
                            Llist = ll.Inserting_inbetween(ll, value,
                                                           int(input('Node to insert after given node')))
                        Llist.Traversal()

                    cont = input('Do you want to continue? Y/N')
                    if cont.lower() == 'N'.lower():
                        flag = False

            elif option == 4:
                print(ll.Traversal())
                flag = True
                while flag:
                    insert = (int(input("""select below option to Delete node in ll
                                1:Delete Node by INDEX
                                2:Delete NOde by VALUE""")))
                    if insert == 1:
                        ll.Traversal()
                        Llist = ll.delete_by_index(ll, int(input('Enter index to delete from LL')))
                        Llist.Traversal()
                    elif insert == 2:
                        ll.Traversal()
                        Llist = ll.delete_by_value(ll, int(input('Enter value to delete from LL')))
                        Llist.Traversal()
                    else:
                        print('Invalid option')


                    cont = input('Do you want to continue? Y/N')
                    if cont == 'N':
                        flag = False

            elif option == 5:
                ll.Traversal()

            elif option == 6:
                sys.exit('Exiting the program !!')

            elif option == 7:
                value = ll.Nth_Node_LL(ll, int(input('Index whose value to be fetched')))
                print('value is {} is at given index'.format(value))


        except Exception as e:
            print('Eceception -->', e)
        finally:
            Continue = input('DO YOU WANT TO CONTINUE DIFFERENT OPTIONS? Y/N')
            if Continue.lower() == 'N'.lower():
                FLAG = False
                sys.exit()
            if Continue.lower() == 'Y'.lower():
                FLAG = True
            else:
                print('INVALID OPTION!!')



