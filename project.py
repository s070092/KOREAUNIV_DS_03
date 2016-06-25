import sys

INFTY = 1E10
sys.setrecursionlimit(10000)

class Adj:
    def __init__(self):
        self.n = 0
        self.next = None

class AdjWeight:
    def __init__(self, n):
        self.n = n
        self.next = None      


class Heap:
    def __init__(self):
        self.nelem = 0
        self.A = []
    def parent(self,n):
        return (n-1)//2
    def left(self,n):
        return 2*n+1
    def right(self,n):
        return 2*n+2
    def compare(self,a,b):
        return a - b > 00
    def exchange(self,i,j):
        A = self.A
        A[i],A[j] = A[j],A[i]
    def heapify(self,i):
        A = self.A
        l = self.left(i)
        r = self.right(i)
        if l < self.nelem and self.compare(A[l], A[i]):
            largest = l
        else:
            largest = i
        if r < self.nelem and self.compare(A[r], A[largest]):
            largest = r
        if largest != i:
            self.exchange(i,largest)
            self.heapify(largest)
            
class PrioNode:
    def __init__(self, key, n):
        self.ndx = 0
        self.n = n
        self.key = key
    def __repr__(self):
        return "(%d:%d,%d)" % (self.ndx,self.n, self.key)

class MaxQueue(Heap):
    def __init__(self):
        super().__init__()
    def compare(self,a,b):
        return a.key > b.key
    def exchange(self,i,j):
        A = self.A
        A[i].ndx = j
        A[j].ndx = i
        super().exchange(i,j)
    def update_key(self,i):
        parent = lambda x: self.parent(i)
        compare = lambda a,b: self.compare(a,b)
        A = self.A
        while i > 0 and not compare(A[parent(i)], A[i]):
            self.exchange(i,parent(i))
            i = parent(i)
    def increase_key(self,i,key):
        A = self.A
        if key < A[i].key:
            print ("Error")
            sys.exit(-1)
        A[i].key = key
        self.update_key(i)
    def insert(self,n):
        A = self.A
        while (len(A) < self.nelem):
            A.append(None)
        i = self.nelem
        A.append(None)
        self.nelem = self.nelem + 1
        A[i] = n
        A[i].ndx = i
        self.update_key(i)
    def extract(self):
        elem = self.A[0]
        self.exchange(0,self.nelem-1)
        self.nelem = self.nelem - 1
        self.heapify(0)
        return elem
    def is_empty(self):
        return self.nelem == 0

class MinQueue(MaxQueue):
    def __init__(self):
        super().__init__()
    def compare(self,a,b):
        return a.key < b.key
    def update_key(self,i):
        parent = lambda x: self.parent(i)
        A = self.A
        while i > 0 and not self.compare(A[parent(i)], A[i]):
            self.exchange(i,parent(i))
            i = parent(i)
    def decrease_key(self,i,key):
        A = self.A
        if key > A[i].key:
            print ("Error")
            sys.exit(-1)
        A[i].key = key
        self.update_key(i)
    def __repr__(self):
        return "%a %a" % (self.nelem,self.A)


class Weight(AdjWeight):
    def __init__(self, n, w):
        super().__init__(n)
        self.w = w

        

class Vertex:
    def __init__(self, name):
        self.parent = -1
        self.name = name
        self.n = 0
        self.first = None
        self.red = False
    def add(self, v):
        a = AdjWeight()
        a.n = v.n
        a.next = self.first
        self.first = a
    def copy(self, other):
        self.parent = other.parent
        self.name = other.name
        self.n = other.n
        self.first = other.first

class DijkVertex(Vertex):
    def __init__(self, name):
        super().__init__(name)
        self.d = INFTY
        self.priority = None
    def __repr__(self):
        return "(%a %a %a)" % (self.name,self.n,self.d)
    def add(self, v, w):
        a = Weight(v, w)
        a.next = self.first
        self.first = a
    def set_priority(self,n):
        self.priority = n
    def decrease_key(self, q):
        prio = self.priority
        ndx = prio.ndx
        q.decrease_key(ndx, self.d)
        

class Dijkstra:
    def __init__(self):
        self.vertices = []
        self.q = MinQueue()
    def add_vertex(self,name):
        n = len(self.vertices)
        v = DijkVertex(name)
        v.n = n
        self.vertices.append(v)
        return v
    def get_vertex(self,name):
        for v in self.vertices:
            if v.name == name:
                return v
        return None        
    def print_vertex(self,n):
        print (self.vertices[n].name, end=' ')
        print (self.vertices[n].parent, end=' ')
        print (self.vertices[n].d, end=' ')
        p = self.vertices[n].first
        while p:
            print (p.n.name, end = ' ')
            print (p.w, end = ' ')
            p = p.next
        print('')
    def print_vertices(self):
        for i in range(len(self.vertices)):
            self.print_vertex(i)
    def relax(self, u):
        vset = self.vertices
        q = self.q
        p = u.first
        while p:
            v = p.n;
            d = u.d + p.w
            if d < v.d:
                v.d = d
                v.parent = u.n
                print(v)
                v.decrease_key(q)
            p = p.next
    def shortest_path(self):
        q = self.q
        vset = self.vertices
        for v in vset:
            n = PrioNode(v.d, v.n)
            v.set_priority(n)
            q.insert(n)
        while not q.is_empty():
            u = q.extract()
            self.relax(vset[u.n])

            


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []
    def create_queue(self,sz):
        self.sz = sz
        self.buf = list(range(sz))  # malloc(sizeof(int)*sz)
    def enqueue(self,val):
        self.buf[self.rear] = val
        self.rear = (self.rear + 1) % self.sz
    def dequeue(self):
        res = self.buf[self.front]
        self.front = (self.front + 1) % self.sz
        return res
    def is_empty(self):
        return self.front == self.rear

def print_vertex(vertices,n):
    print (vertices[n].name, end=' ')
    print (vertices[n].color, end=' ')
    print (vertices[n].parent, end=' ')
    print (vertices[n].d, end=':')
    p = vertices[n].first
    while p:
        print (vertices[p.n].name, end = ' ')
        p = p.next
    print('')

def g_transpose(vertices, vertices1):
    for i in range(len(vertices1)):
        vertices1[i].first = None
    for v in vertices:
        p = v.first
        while p:
            vertices1[p.n].add(v)
            p = p.next

class DepthFirstSearch:
    def __init__(self):
        self.time = 0;
        self.vertices = None
    def set_vertices(self,vertices):
        self.vertices = vertices
        for i in range(len(self.vertices)):
            self.vertices[i].n = i
    def dfs(self):
        for u in self.vertices:
            u.color = WHITE
            u.parent = -1
        self.time = 0
        for u in self.vertices:
            if u.color == WHITE:
                self.dfs_visit(u)
    def dfs_visit(self, u):
        self.time = self.time + 1
        u.d = self.time
        u.color = GRAY
        v = u.first
        while v:
            if self.vertices[v.n].color == WHITE:
                self.vertices[v.n].parent = u.n
                self.dfs_visit(self.vertices[v.n])
            v = v.next;
        u.color = BLACK
        self.time = self.time + 1
        u.f = self.time

    def print_scc(self, u):
        print(u.name, end=" ")
        vset = self.vertices
        if u.parent >= 0:
            self.print_scc(vset[u.parent])
        
    def scc_find(self, u):
        u.color = GRAY
        v = u.first
        found = False
        while v:
            if self.vertices[v.n].color == WHITE:
                found = True
                self.vertices[v.n].parent = u.n
                self.scc_find(self.vertices[v.n])
            v = v.next;
        if not found:
            print("SCC:", end=" ")
            self.print_scc(u)
            print ("")
        u.color = BLACK
        
    def print_vertex(self,n):
        print (self.vertices[n].name, end=' ')
        print (self.vertices[n].color, end=' ')
        print (self.vertices[n].parent, end=' ')
        print (self.vertices[n].d, end=' ')
        print (self.vertices[n].f, end=':')
        p = self.vertices[n].first
        while p:
            print (self.vertices[p.n].name, end = ' ')
            p = p.next
        print('')
    def print_vertices(self):
        for i in range(len(self.vertices)):
            self.print_vertex(i)
    def transpose(self):
        vertices1 = []
        for v in self.vertices:
            v1 = Int_Vertex_Friend(v.name)
            v1.copy(v)
            vertices1.append(v1)
        g_transpose(self.vertices,vertices1)
        self.set_vertices(vertices1)

    def left(self,n):
        return 2*n+1

    def right(self,n):
        return 2*n+2

    def heapify(self,A,i,heapsize):
        vset = self.vertices
        l = self.left(i)
        r = self.right(i)
        if l < heapsize and vset[A[l]].f < vset[A[i]].f:
            largest = l
        else:
            largest = i
        if r < heapsize and vset[A[r]].f < vset[A[largest]].f:
            largest = r
        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            self.heapify(A,largest,heapsize)

    def buildheap(self,A):
        for i in range(len(A)//2 + 1,0,-1):
            self.heapify(A,i-1,len(A))

    def heapsort(self,A):
        self.buildheap(A)
        for i in range(len(A),1,-1):
            A[i-1],A[0] = A[0],A[i-1]
            self.heapify(A,0,i - 1)
        
    def sort_by_f(self):
        vset = self.vertices
        sorted_indices = list(range(len(vset)))
        self.heapsort(sorted_indices)
        return sorted_indices
    
    def scc(self):
        self.dfs()
        self.transpose()
        sorted = self.sort_by_f()
        vset = self.vertices
        for v in vset:
            v.color = WHITE
            v.parent = -1
        for n in sorted:
            if self.vertices[n].color == WHITE:
                self.scc_find(vset[n])






class Vertex_User:
    def __init__(self):
        self.n = 0;
        self.id = 0
        self.date = ""
        self.name = ""
        self.user_count = 0
        self.friend_count = 0
        self.tweet_count = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None
        self.red = False
    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a
    def copy(self, other):
        self.parent = other.parent
        self.name = other.name
        self.n = other.n
        self.first = other.first        
        

class Int_Vertex_User(Vertex_User):
    def __init__(self):
        super().__init__()
        self.id = 0
    def less_than(self,other):
        return self.id < other.id
    def make_node(self,id, date, name):
        n = Int_Vertex_User()
        n.id = id
        n.date = date.replace('\n', '')
        n.name = name.replace('\n', '')    
        return n
    def print_node(self):
        print(self.id)



WHITE = 0
GRAY = 1
BLACK = 2


        
class Vertex_Friend:
    def __init__(self, name):
        self.color = WHITE
        self.parent = -1
        self.name = name        
        self.n = 0
        self.id = 0
        self.friend_id = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None
        self.red = False
    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a
    def copy(self, other):
        self.color = other.color
        self.parent = other.parent
        self.name = other.name
        self.n = other.n
        self.first = other.first        
        

class Int_Vertex_Friend(Vertex_Friend):
    def __init__(self, name):
        super().__init__(name)
        self.id = 0
        self.d = 0
        self.f = 0        
    def less_than(self,other):
        return self.id < other.id
    def make_node(self,id, friend_id):
        n = Int_Vertex_Friend("")
        n.id = id
        n.friend_id = friend_id
        return n
    def print_node(self):
        print(self.id)
    def copy(self, other):
        super().copy(other)
        self.d = other.d
        self.f = other.f        
        


class Vertex_Word:
    def __init__(self):
        self.n = 0
        self.id = 0
        self.date = ""
        self.word = ""
        self.word_count = 0
        self.user_count = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None
        self.red = False

class Int_Vertex_Word(Vertex_Word):
    def __init__(self):
        super().__init__()
        self.word = 0
    def less_than(self,other):
        return self.word < other.word

    def make_node(self,id, date, word):
        n = Int_Vertex_Word()
        n.id = id
        n.date = date.replace('\n', '')
        n.word = word.replace('\n', '')
        return n
    def print_node(self):
     #   print(self.word, self.id, self.p.id, self.p.p.id)
        print(self.word)


class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None

class List:
    def __init__(self):
        self.first = None
    def add(self, val):
        p = self.first
        while p is not None:
            if p.val == val:
                return None
            p = p.next;
        if p == None :
            node = ListNode()
            node.val = val;
            if self.first is None:
                self.first = node
            else:
                node.next = self.first
                self.first = node
        return None
    def print(self):
        p = self.first
        if p == None :
            return 1      
        while p is not None:
            print(p.val)
            p = p.next;
        return None


        

class RedBlackTree:
    def __init__(self):
        self.root = None
    def insert(self,z):
        y = None
        x = self.root
        while x:
            y = x
            if z.less_than(x):
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.less_than(y):
            y.left = z
        else:
            y.right = z
            
        z.left = None
        z.right = None
        z.red = True
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p != None and z.p.red:
            if z.p.p != None:
                if z.p == z.p.p.left:
                    y = z.p.p.right
                    if y != None :
                        if y.red:
                            z.p.red = False
                            y.red = False
                            z.p.p.red = True
                            z = z.p.p
                        else:
                            if z == z.p.right:
                                z = z.p
                                self.left_rotate(z)
                            z.p._red = False
                            z.p.p._red = True
                            self.right_rotate(z.p.p)
                    else :
                        break
                else :
                    break
            else:
                if z.p.p != None:
                    y = z.p.p.left
                    if y.red:
                        z.p.red = False
                        y._red = False
                        z.p.p._red = True
                        z = z.p.p
                    else:
                        if z == z.p.left:
                            z = z.p
                            self._right_rotate(z)
                        z.p.red = False
                        z.p.p.red = True
                        self.left_rotate(z.p.p)
                else :
                    break
                self.root.red = False



        
    def delete(self,z):
        y = z
        y_original_color = y.red
        if z == None:
            print("No data : delete 할 data 가 없습니다. (root == Null)")
            return None
        elif z.left == None:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == None:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.red
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
        if y_original_color == False :
            self.delete_fixup(x)


    
    def delete_fixup(self,x):
        while x != self.root and x.red == False :
            if x == x.p.left :
                w = x.p.right
                if w.red == True :
                    w.red = False
                    x.p.red = True
                    left_rotate(self, x.p)
                    w= w.p.right
                if w.left.red == False and w.right.red == False :
                    w.red = True
                    x = x.p
                else :
                    if w.right.red == False :
                        w.left.red = False
                        w.red = True
                        right_rotate(self, w)
                        w = x.p.right
                    w.red = x.p.red
                    x.p.red = False
                    w.right.red = False
                    left_rotate(self, x.p)
                    x = self.root
            else :
                w = x.p.left
                if w.red == True :
                    w.red = False
                    x.p.red = True
                    right_rotate(self, x.p)
                    w= w.p.left
                if w.right.red == False and w.left.red == False :
                    w.red = True
                    x = x.p
                else :
                    if w.left.red == False :
                        w.right.red = False
                        w.red = True
                        left_rotate(self, w)
                        w = x.p.left
                    w.red = x.p.red
                    x.p.red = False
                    w.left.red = False
                    right_rotate(self, x.p)
                    x = self.root
        x.red = False

            
    def minimum(self, x):
        if None == x:
            x = self.root
        while x.left != None:
            x = x.left
        return x
    
    def maximum(self, x):
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.p = x
        y.p = x.p
        if x.p == None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y


    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != None:
            x.right.p = y
        x.p = y.p
        if y.p == None:
            self.root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x
    
    
    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p
            
    def print_util(self, tree, level):
        if self.root == None :
            print("값이 없습니다.")
            return 1
        if (tree.right):
            self.print_util(tree.right, level + 1)
        for i in range(level):
            print('    ', end = '')
        tree.print_node()
        if (tree.left):
            self.print_util(tree.left, level + 1)
    def print_tree(self):
        self.print_util(self.root, 0)




def menu_interface():
    print("\n0. Read data files")
    print("1. display statistics")
    print("2. Top 5 most tweeted words")
    print("3. Top 5 most tweeted users")
    print("4. Find users who tweeted a word (e.g., ’연세대’)")
    print("5. Find all people who are friends of the above users")
    print("6. Delete all mentions of a word")
    print("7. Delete all users who mentioned a word")
    print("8. Find strongly connected components")
    print("9. Find shortest path from a given user")
    print("99. Quit")
    print("Select Menu:")
    
rbt_user = RedBlackTree()
rbt_friend = RedBlackTree()
rbt_word = RedBlackTree()

list_user_mentioned = List()
list_friend = List()
list_friend = List()
list_word = List()
list_word_friend = List()



def menu0():


    rbt_user.__init__()
    rbt_friend.__init__()
    rbt_word.__init__()
    
    proto_user = Int_Vertex_User()

    user_file = open('user.txt')
    global user_number
    user_number = 0

    line_count = 1
    for line in user_file:
        line_count += 1
     
    user_number = int(line_count/4)

    user_file = open('user.txt')
    line_count = -1
    for line in user_file:
        line_count += 1
 
        if line_count%4 == 0 :
            temp_id = int(line)  
        elif line_count%4 == 1 :
            temp_date = line
        elif line_count%4 == 2 :
            temp_name = line
            rbt_user.insert(proto_user.make_node(temp_id, temp_date.replace('\n', ''), temp_name.replace('\n', '')))


    proto_friend = Int_Vertex_Friend("")

    friend_file = open('friend.txt')
    global friend_number
    friend_number = 0

    line_count = 1
    for line in friend_file:
        line_count += 1
     
    friend_number = int(line_count/3)

    friend_file = open('friend.txt')
    line_count = -1
    for line in friend_file:
        line_count += 1
 
        if line_count%3 == 0 :
            temp_id = int(line)
        elif line_count%3 == 1 :
            temp_friend_id = int(line)
            rbt_friend.insert(proto_friend.make_node(temp_id, temp_friend_id))



    proto_word = Int_Vertex_Word()

    word_file = open('word.txt')
    word_number = 0

    line_count = 1
    for line in word_file:
        line_count += 1
     
    word_number = int(line_count/4)
    
    word_file = open('word.txt')
    line_count = -1
    for line in word_file:
        line_count += 1
 
        if line_count%4 == 0 :
            temp_id = int(line)
        elif line_count%4 == 1 :
            temp_date = line
        elif line_count%4 == 2 :
            temp_word = line
            rbt_word.insert(proto_word.make_node(temp_id, temp_date.replace('\n', ''), temp_word.replace('\n', '')))

    print("Total users:", user_number)
    print("Total friendship records:", friend_number)
    print("Total tweets:", word_number)

    return rbt_user, rbt_friend, rbt_word





def statistics_friend_user(rbt_user, rbt_friend):
    if(rbt_user.right):
        statistics_friend_user(rbt_user.right, rbt_friend)
    if(rbt_user.id == rbt_friend.id):
        rbt_user.friend_count += 1
    if(rbt_user.left):
        statistics_friend_user(rbt_user.left, rbt_friend)


def statistics_friend(rbt_user, rbt_friend):
    if (rbt_friend.right):
        statistics_friend(rbt_user, rbt_friend.right)
    statistics_friend_user(rbt_user, rbt_friend)
    if (rbt_friend.left):
        statistics_friend(rbt_user, rbt_friend.left)

def statistics_friend_cal(rbt_user, total_number, user_number, min_friend, max_friend):
    if (rbt_user.right) :
        total_number, user_number, min_friend, max_friend = statistics_friend_cal(rbt_user.right, total_number, user_number, min_friend, max_friend)
    total_number += rbt_user.friend_count
    user_number += 1
    if rbt_user.friend_count < min_friend :
        min_friend = rbt_user.friend_count      
    if rbt_user.friend_count > max_friend :
        max_friend = rbt_user.friend_count      
    if (rbt_user.left) :
        total_number, user_number, min_friend, max_friend = statistics_friend_cal(rbt_user.left, total_number, user_number, min_friend, max_friend)

    return total_number, user_number, min_friend, max_friend
        


def statistics_tweets_user(rbt_user, rbt_word):
    if (rbt_user.right):
        statistics_tweets_user(rbt_user.right, rbt_word)
    if(rbt_user.id == rbt_word.id):
        rbt_user.tweet_count += 1
    if (rbt_user.left):
        statistics_tweets_user(rbt_user.left, rbt_word)

def statistics_tweets(rbt_user, rbt_word):
    if (rbt_word.right):
        statistics_tweets(rbt_user, rbt_word.right)
    statistics_tweets_user(rbt_user, rbt_word)    
    if (rbt_word.left):
        statistics_tweets(rbt_user, rbt_word.left)         


def statistics_tweets_cal(rbt_user, total_tweet, tweet_count, min_tweet, max_tweet):
    if (rbt_user.right) :
        total_tweet, tweet_count, min_tweet, max_tweet = statistics_tweets_cal(rbt_user.right, total_tweet, tweet_count, min_tweet, max_tweet)
    total_tweet += rbt_user.tweet_count
    tweet_count += 1
    if rbt_user.tweet_count < min_tweet :
        min_tweet = rbt_user.tweet_count      
    if rbt_user.tweet_count > max_tweet :
        max_tweet = rbt_user.tweet_count 
    if (rbt_user.left) :
        total_tweet, tweet_count, min_tweet, max_tweet = statistics_tweets_cal(rbt_user.left, total_tweet, tweet_count, min_tweet, max_tweet)

    return total_tweet, tweet_count, min_tweet, max_tweet












def menu1():
    total_number = 0
    user_number = 0
    min_friend = 1E10    
    max_friend = 0

    total_tweet = 0
    tweet_count = 0
    min_tweet = 1E10
    max_tweet = 0


    statistics_friend(rbt_user.root, rbt_friend.root)


    total_number, user_number, min_friend, max_friend = statistics_friend_cal(rbt_user.root, total_number, user_number, min_friend, max_friend) 
    print("Average number of friends:", total_number/user_number)
    print("Minimum number of friends:", min_friend)
    print("Maximum number of friends:", max_friend, "\n")

    statistics_tweets(rbt_user.root, rbt_word.root)

    total_tweet, tweet_count, min_tweet, max_tweet = statistics_tweets_cal(rbt_user.root, total_tweet, tweet_count, min_tweet, max_tweet)
    print("Average tweets per user:", total_tweet/tweet_count)
    print("Minimum tweets per user:", min_tweet)
    print("Maximum tweets per user:", max_tweet)





       

def statistics_tweets_count(rbt_word, rbt_word1, most_word1, most_word1_count):
    if (rbt_word.right):
        most_word1, most_word1_count = statistics_tweets_count(rbt_word.right, rbt_word1, most_word1, most_word1_count)

    if rbt_word.word == rbt_word1.word:
        rbt_word1.word_count += 1
        if rbt_word1.word_count > most_word1_count:
           most_word1 = rbt_word1.word
           most_word1_count = rbt_word1.word_count
    if (rbt_word.left):
        most_word1, most_word1_count = statistics_tweets_count(rbt_word.left, rbt_word1, most_word1, most_word1_count)        
    return most_word1, most_word1_count



def statistics_tweets_count1(rbt_word1, most_word1, most_word1_count):
    if (rbt_word1.right):
        most_word1, most_word1_count = statistics_tweets_count1(rbt_word1.right, most_word1, most_word1_count)
    most_word1, most_word1_count = statistics_tweets_count(rbt_word.root, rbt_word1, most_word1, most_word1_count)
    if (rbt_word1.left):
        most_word1, most_word1_count = statistics_tweets_count1(rbt_word1.left, most_word1, most_word1_count)   
    return  most_word1, most_word1_count

def statistics_tweets_count2(rbt_word1, most_word1, most_word2, most_word2_count):
    if (rbt_word1.right):
        most_word1, most_word2, most_word2_count = statistics_tweets_count2(rbt_word1.right, most_word1, most_word2, most_word2_count)
    if most_word1 != rbt_word1.word :
        most_word2, most_word2_count = statistics_tweets_count(rbt_word.root, rbt_word1, most_word2, most_word2_count)
    if (rbt_word1.left):
        most_word1, most_word2, most_word2_count = statistics_tweets_count2(rbt_word1.left, most_word1, most_word2, most_word2_count)   
    return  most_word1, most_word2, most_word2_count

def statistics_tweets_count3(rbt_word1, most_word1, most_word2, most_word3, most_word3_count):
    if (rbt_word1.right):
        most_word1, most_word2, most_word3, most_word3_count = statistics_tweets_count3(rbt_word1.right, most_word1, most_word2, most_word3, most_word3_count)
    if ((most_word1 != rbt_word1.word) and (most_word2 != rbt_word1.word)) :
        most_word3, most_word3_count = statistics_tweets_count(rbt_word.root, rbt_word1, most_word3, most_word3_count)
    if (rbt_word1.left):
        most_word1, most_word2, most_word3, most_word3_count = statistics_tweets_count3(rbt_word1.left, most_word1, most_word2, most_word3, most_word3_count)   
    return  most_word1, most_word2, most_word3, most_word3_count

def statistics_tweets_count4(rbt_word1, most_word1, most_word2, most_word3, most_word4, most_word4_count):
    if (rbt_word1.right):
        most_word1, most_word2, most_word3, most_word4, most_word4_count = statistics_tweets_count4(rbt_word1.right, most_word1, most_word2, most_word3, most_word4, most_word4_count)
    if ((most_word1 != rbt_word1.word) and (most_word2 != rbt_word1.word) and (most_word3 != rbt_word1.word)) :
        most_word4, most_word4_count = statistics_tweets_count(rbt_word.root, rbt_word1, most_word4, most_word4_count)
    if (rbt_word1.left):
        most_word1, most_word2, most_word3, most_word4, most_word4_count = statistics_tweets_count4(rbt_word1.left, most_word1, most_word2, most_word3, most_word4, most_word4_count)   
    return  most_word1, most_word2, most_word3, most_word4, most_word4_count


def statistics_tweets_count5(rbt_word1, most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count):
    if (rbt_word1.right):
        most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count = statistics_tweets_count5(rbt_word1.right, most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count)
    if ((most_word1 != rbt_word1.word) and (most_word2 != rbt_word1.word) and (most_word3 != rbt_word1.word) and (most_word4 != rbt_word1.word)) :
        most_word5, most_word5_count = statistics_tweets_count(rbt_word.root, rbt_word1, most_word5, most_word5_count)
    if (rbt_word1.left):
        most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count = statistics_tweets_count5(rbt_word1.left, most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count)   
    return  most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count

def rbt_word_init(rbt_word1):
    if (rbt_word1.right):
        rbt_word_init(rbt_word1.right)
    rbt_word1.word_count = 0
    rbt_word1.user_count = 0
    if (rbt_word1.left):
        rbt_word_init(rbt_word1.left)
    return rbt_word1










def menu2():
    most_word1 = ""
    most_word1_count = 0

    most_word2 = ""
    most_word2_count = 0

    most_word3 = ""
    most_word3_count = 0    

    most_word4 = ""
    most_word4_count = 0

    most_word5 = ""
    most_word5_count = 0      


    print("Top 5 most tweeted words\n")
    
    rbt_word1 = rbt_word
    most_word1, most_word1_count = statistics_tweets_count1(rbt_word1.root, most_word1, most_word1_count)
    print("1:\t", most_word1, "\t", most_word1_count)
    rbt_word1.root = rbt_word_init(rbt_word1.root)

    most_word1, most_word2, most_word2_count = statistics_tweets_count2(rbt_word1.root, most_word1, most_word2, most_word2_count)
    print("2:\t", most_word2, "\t", most_word2_count)
    
    rbt_word1.root = rbt_word_init(rbt_word1.root)    
    most_word1, most_word2, most_word3, most_word3_count = statistics_tweets_count3(rbt_word1.root, most_word1, most_word2, most_word3, most_word3_count)
    print("3:\t", most_word3, "\t", most_word3_count)
    
    rbt_word1.root = rbt_word_init(rbt_word1.root)
    most_word1, most_word2, most_word3, most_word4, most_word4_count = statistics_tweets_count4(rbt_word1.root, most_word1, most_word2, most_word3, most_word4, most_word4_count)
    print("4:\t", most_word4, "\t", most_word4_count)
    
    rbt_word1.root = rbt_word_init(rbt_word1.root)
    most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count = statistics_tweets_count5(rbt_word1.root, most_word1, most_word2, most_word3, most_word4, most_word5_count, most_word5_count)
    print("5:\t", most_word5, "\t", most_word5_count) 






def statistics_tweets_user_count(rbt_word, rbt_word1, most_user1, most_user1_count):
    if (rbt_word.right):
        most_user1, most_user1_count = statistics_tweets_user_count(rbt_word.right, rbt_word1, most_user1, most_user1_count)

    if rbt_word.id == rbt_word1.id:
        rbt_word1.user_count += 1
        if rbt_word1.user_count > most_user1_count:
           most_user1 = rbt_word1.id
           most_user1_count = rbt_word1.user_count

    if (rbt_word.left):
        most_user1, most_user1_count = statistics_tweets_user_count(rbt_word.left, rbt_word1, most_user1, most_user1_count)        
    return most_user1, most_user1_count



def statistics_tweets_user_count1(rbt_word1, most_user1, most_user1_count):
    if (rbt_word1.right):
        most_user1, most_user1_count = statistics_tweets_user_count1(rbt_word1.right, most_user1, most_user1_count)
    most_user1, most_user1_count = statistics_tweets_user_count(rbt_word.root, rbt_word1, most_user1, most_user1_count)
    if (rbt_word1.left):
        most_user1, most_user1_count = statistics_tweets_user_count1(rbt_word1.left, most_user1, most_user1_count)   
    return  most_user1, most_user1_count

def statistics_tweets_user_count2(rbt_word1, most_user1, most_user2, most_user2_count):
    if (rbt_word1.right):
        most_user1, most_user2, most_user2_count = statistics_tweets_user_count2(rbt_word1.right, most_user1, most_user2, most_user2_count)
    if most_user1 != rbt_word1.id :
        most_user2, most_user2_count = statistics_tweets_user_count(rbt_word.root, rbt_word1, most_user2, most_user2_count)
    if (rbt_word1.left):
        most_user1, most_user2, most_user2_count = statistics_tweets_user_count2(rbt_word1.left, most_user1, most_user2, most_user2_count)   
    return  most_user1, most_user2, most_user2_count

def statistics_tweets_user_count3(rbt_word1, most_user1, most_user2, most_user3, most_user3_count):
    if (rbt_word1.right):
        most_user1, most_user2, most_user3, most_user3_count = statistics_tweets_user_count3(rbt_word1.right, most_user1, most_user2, most_user3, most_user3_count)
    if ((most_user1 != rbt_word1.id) and (most_user2 != rbt_word1.id)) :
        most_user3, most_user3_count = statistics_tweets_user_count(rbt_word.root, rbt_word1, most_user3, most_user3_count)
    if (rbt_word1.left):
        most_user1, most_user2, most_user3, most_user3_count = statistics_tweets_user_count3(rbt_word1.left, most_user1, most_user2, most_user3, most_user3_count)   
    return  most_user1, most_user2, most_user3, most_user3_count

def statistics_tweets_user_count4(rbt_word1, most_user1, most_user2, most_user3, most_user4, most_user4_count):
    if (rbt_word1.right):
        most_user1, most_user2, most_user3, most_user4, most_user4_count = statistics_tweets_user_count4(rbt_word1.right, most_user1, most_user2, most_user3, most_user4, most_user4_count)
    if ((most_user1 != rbt_word1.id) and (most_user2 != rbt_word1.id) and (most_user3 != rbt_word1.id)) :
        most_user4, most_user4_count = statistics_tweets_user_count(rbt_word.root, rbt_word1, most_user4, most_user4_count)
    if (rbt_word1.left):
        most_user1, most_user2, most_user3, most_user4, most_user4_count = statistics_tweets_user_count4(rbt_word1.left, most_user1, most_user2, most_user3, most_user4, most_user4_count)   
    return  most_user1, most_user2, most_user3, most_user4, most_user4_count    

def statistics_tweets_user_count5(rbt_word1, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count):
    if (rbt_word1.right):
        most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count = statistics_tweets_user_count5(rbt_word1.right, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count)
    if ((most_user1 != rbt_word1.id) and (most_user2 != rbt_word1.id) and (most_user3 != rbt_word1.id) and (most_user4 != rbt_word1.id)) :
        most_user5, most_user5_count = statistics_tweets_user_count(rbt_word.root, rbt_word1, most_user5, most_user5_count)
    if (rbt_word1.left):
        most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count = statistics_tweets_user_count5(rbt_word1.left, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count)   
    return  most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count


def menu3():
    most_user1 = 0
    most_user1_count = 0

    most_user2 = 0
    most_user2_count = 0

    most_user3 = 0
    most_user3_count = 0    

    most_user4 = 0
    most_user4_count = 0

    most_user5 = 0
    most_user5_count = 0      


    print("Top 5 most tweeted users\n")
    
    rbt_word1 = rbt_word
    most_user1, most_user1_count = statistics_tweets_user_count1(rbt_word1.root, most_user1, most_user1_count)
    print("1:\t", most_user1, "\t", most_user1_count)

    rbt_word1.root = rbt_word_init(rbt_word1.root)
    most_user1, most_user2, most_user2_count = statistics_tweets_user_count2(rbt_word1.root, most_user1, most_user2, most_user2_count)
    print("2:\t", most_user2, "\t", most_user2_count)

    rbt_word1.root = rbt_word_init(rbt_word1.root)
    most_user1, most_user2, most_user3, most_user3_count = statistics_tweets_user_count3(rbt_word1.root, most_user1, most_user2, most_user3, most_user3_count)
    print("3:\t", most_user3, "\t", most_user3_count)

    rbt_word1.root = rbt_word_init(rbt_word1.root)
    most_user1, most_user2, most_user3, most_user4, most_user4_count = statistics_tweets_user_count4(rbt_word1.root, most_user1, most_user2, most_user3, most_user4, most_user4_count)
    print("4:\t", most_user4, "\t", most_user4_count)

    rbt_word1.root = rbt_word_init(rbt_word1.root)
    most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count = statistics_tweets_user_count5(rbt_word1.root, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count)
    print("5:\t", most_user5, "\t", most_user5_count)






    

      



def find_user_name(rbt_user, list_user_mentioned) :
    if rbt_user == None :
        return None
    elif rbt_user.id == list_user_mentioned.val :
        print(rbt_user.id, "\t", rbt_user.name, "\t", rbt_user.date)


    elif rbt_user.id < list_user_mentioned.val :
        find_user_name(rbt_user.right, list_user_mentioned)
        
    elif rbt_user.id > list_user_mentioned.val :
        find_user_name(rbt_user.left, list_user_mentioned)
    
def find_user_mentioned(rbt_word, tweeted_word):
    if rbt_word == None :
        return 1
    if rbt_word.word < tweeted_word :
        find_user_mentioned(rbt_word.right, tweeted_word) 
    elif rbt_word.word == tweeted_word :
        list_user_mentioned.add(rbt_word.id)
        find_user_mentioned(rbt_word.right, tweeted_word)            
    elif rbt_word.word > tweeted_word :
        find_user_mentioned(rbt_word.left, tweeted_word)

def find_list_user_name(list_user_mentioned) :
    if list_user_mentioned == None :
        return None
    find_user_name(rbt_user.root, list_user_mentioned)
    find_list_user_name(list_user_mentioned.next)



    
def menu4():

    list_user_mentioned.__init__()
    print("Find users who tweeted a word (e.g., '연세대')")
    print("Input a word:")    
    tweeted_word = input()
    find_user_mentioned(rbt_word.root, tweeted_word)
    
    absent = list_user_mentioned.print()
    if absent != 1 :
        print("\nname, 가입일시도 확인하시려면 1번을 누르시고,")
        print("메뉴 인터페이스로 돌아가시려면 2번을 누르세요")
        print("입력하세요:")
        name_check = input()
        if name_check == "1":
            find_list_user_name(list_user_mentioned.first)
            return 0
        else :
            return 1

def find_list_user_friend(rbt_friend, list_user_mentioned) :

    if rbt_friend == None :
        return None
    elif rbt_friend.id < list_user_mentioned.val :
        find_list_user_friend(rbt_friend.right, list_user_mentioned)
    elif rbt_friend.id == list_user_mentioned.val :
        list_friend.add(rbt_friend.friend_id)
        find_list_user_friend(rbt_friend.right, list_user_mentioned)
    elif rbt_friend.id > list_user_mentioned.val :
        find_list_user_friend(rbt_friend.left, list_user_mentioned)

def find_user_friend(list_user_mentioned) :
    while list_user_mentioned != None :
        find_list_user_friend(rbt_friend.root, list_user_mentioned)
        list_user_mentioned = list_user_mentioned.next






def find_friend_name(rbt_user, list_friend_id) :
    if rbt_user == None :
        return None
    if rbt_user.id == list_friend_id :
        print(rbt_user.id, "\t", rbt_user.name, "\t", rbt_user.date)


    elif rbt_user.id < list_friend_id :
        find_friend_name(rbt_user.right, list_friend_id)
        
    elif rbt_user.id > list_friend_id :
        find_friend_name(rbt_user.left, list_friend_id)

        
def find_list_friend_name(list_friend) :
    if list_friend == None :
        return None
    find_friend_name(rbt_user.root, list_friend.val)
    find_list_friend_name(list_friend.next)


def menu5() :
    list_friend.__init__()

    find_user_friend(list_user_mentioned.first)

    absent = list_friend.print()
    if absent != 1 :
        print("\nname, 가입일시도 확인하시려면 1번을 누르시고,")
        print("메뉴 인터페이스로 돌아가시려면 2번을 누르세요")
        print("입력하세요:")
        name_check = input()
        if name_check == "1":
            find_list_friend_name(list_friend.first)
            return 0
        else :
            return 1
    else :
        print("친구분이 계시지 않습니다. 4번 메뉴를 실행하셨는지 확인하세요.")
        return 0
              






def delete_node(node_delete) :
    rbt_word.delete(node_delete)

def delete_word(rbt_word, tweeted_word):
    
        
    if rbt_word == None :
        return None
        
    if rbt_word.word < tweeted_word :
        if rbt_word.right == None :
            delete_word(rbt_word.left, tweeted_word)
        else :
            delete_word(rbt_word.right, tweeted_word)

    elif rbt_word.word == tweeted_word :

        list_word.add(rbt_word.id)
        node_delete = rbt_word    
        delete_node(node_delete)

        if rbt_word.right == None :
            delete_word(rbt_word.left, tweeted_word)
        else :
            delete_word(rbt_word.right, tweeted_word)   
        
    elif rbt_word.word > tweeted_word :
        if rbt_word.left == None :
            delete_word(rbt_word.right, tweeted_word)
        else :
            delete_word(rbt_word.left, tweeted_word)
        

def menu6():
    list_word.__init__()
    print("Delete all mentions of a word")
    print("Input a word:")
    tweeted_word = input()
    
    delete_word(rbt_word.root, tweeted_word)
    print("Delete complete (", tweeted_word, ")")

    

def delete_list_user(node_delete_user):
    rbt_user.delete(node_delete_user)

def delete_user(rbt_user, list_word):
    if rbt_user == None :
        return 0
    if rbt_user.id < list_word.val :
        delete_user(rbt_user.right, list_word)
    elif rbt_user.id == list_word.val :
        list_word_friend.add(rbt_user.id)
        node_delete_user = rbt_user
        delete_list_user(node_delete_user)
    elif rbt_user.id > list_word.val :
        delete_user(rbt_user.left, list_word)
        
def delete_list_word(list_word):
    if list_word != None :
        delete_user(rbt_user.root, list_word)
        delete_list_word(list_word.next)
        

def delete_list_friend_id(node_delete_friend):
    rbt_friend.delete(node_delete_friend)

def delete_friend_id(rbt_friend, list_word_friend):
    if rbt_friend == None :
        return 0
    if rbt_friend.id < list_word_friend.val :
        delete_friend_id(rbt_friend.right, list_word_friend)
    elif rbt_friend.id == list_word_friend.val :
        node_delete_friend = rbt_friend
        delete_list_friend_id(node_delete_friend)

        if rbt_friend.right == None :
            delete_friend_id(rbt_friend.left, list_word_friend)  
        if rbt_friend.left == None :
            delete_friend_id(rbt_friend.right, list_word_friend)

        
    elif rbt_friend.id > list_word_friend.val :
        delete_friend_id(rbt_friend.left, list_word_friend)






        
        

def delete_friend(list_word_friend):
    if list_word_friend != None :
        delete_friend_id(rbt_friend.root, list_word_friend)
        delete_friend(list_word_friend.next)

def delete_list_friend_friendid(node_delete_friend):
    rbt_friend.delete(node_delete_friend)


def delete_friend_id(rbt_friend, list_word_friend):
    if(rbt_friend.right):
        delete_friend_id(rbt_friend.right, list_word_friend)
    
    if rbt_friend.friend_id == list_word_friend.val :
        node_delete_friend = rbt_friend
        delete_list_friend_friendid(node_delete_friend)    
    if(rbt_friend.left):
        delete_friend_id(rbt_friend.left, list_word_friend)



def delete_friendid(list_word_friend):
    if list_word_friend != None :
        delete_friendid(list_word_friend.next)
        
def menu7():
    list_word_friend.__init__()    
    print("Delete all users who mentioned a word")
    delete_list_word(list_word.first)
    print("Complete.\n")
    print("Deleting the nodes in the friend tree (the id in the friend tree == the id in the user tree)...")
    delete_friend(list_word_friend.first)
    print("Complete.\n")
    print("Deleting the nodes in the friend tree (the friend_id in the friend tree == the id in the user tree)...")
    delete_friendid(list_word_friend.first)    
    print("Complete.\n")



        



array_count_friend_id = 0

def array_init7(rbt_friend):
    global array_count
    if (rbt_friend.right):
        array_init(rbt_friend.right)
    dup_check = 0
    for i in range(len(vertices_friend)):
        print("88 ", i)
        if vertices_friend[array_count-1] == None :
            print("88888")
            continue
        if vertices_friend[array_count].name == rbt_friend.id :
            print("7 ", rbt_friend.id )
    vertices_friend[array_count] = Int_Vertex_Friend(rbt_friend.id)
    array_count += 1
    if (rbt_friend.left):
        array_init(rbt_friend.left)


def array_init_friend_id(rbt_friend):
    global array_count_friend_id
    if (rbt_friend.right):
        array_init_friend_id(rbt_friend.right)

    vertices_friend_friend_id[array_count_friend_id] = Int_Vertex_Friend(rbt_friend.friend_id)
    array_count_friend_id += 1
   # print("78   ", array_count_friend_id, vertices_friend_friend_id[array_count_friend_id-1].name)    
    if (rbt_friend.left):
        array_init_friend_id(rbt_friend.left)
        

def vertices_add(rbt_friend, vertices_user):
    if (rbt_friend.right):
        vertices_add(rbt_friend.right, vertices_user)
        
    for i in range(len(vertices_user)):
        if(rbt_friend.id == vertices_user[i].id):
            for j in range(len(vertices_user)):
                if(rbt_friend.friend_id == vertices_user[j].id):
                    vertices_user[i].add(vertices_user[j])

    if (rbt_friend.left):
        vertices_add(rbt_friend.left, vertices_user)



def array_init(rbt_user):
    global array_count8
    if (rbt_user.right):
        array_init(rbt_user.right)

    vertices_user[array_count8] = rbt_user
    vertices_user[array_count8].n = array_count8
    array_count8 = array_count8+1
    if (rbt_user.left):
        array_init(rbt_user.left)
        

def menu8():
    print("Find strongly connected components")
    global array_count8
    array_count8 = 0

    global vertices_user


    vertices_user = [None]*user_number
    
    array_init(rbt_user.root)
    DFS = DepthFirstSearch()
    DFS.set_vertices(vertices_user)


    vertices_add(rbt_friend.root, vertices_user)


    DFS.scc()
   # DFS.print_vertices()


     



def array_init9(rbt_user):
    global array_count9
    if (rbt_user.right):
        array_init9(rbt_user.right)

    vertices_user9[array_count9] = rbt_user.id
    array_count9 = array_count9+1
    if (rbt_user.left):
        array_init9(rbt_user.left)
        

def add_friend(rbt_friend, v):
    print(rbt_friend.id, v.name)
    if rbt_friend == None :
        return 0
    if rbt_friend.id < v.name :
        add_friend(rbt_friend.right, v)
    elif rbt_friend.id == v.name :
        print(8)
    elif rbt_friend.id < v.name :
        add_friend(rbt_friend.right, v)

        
def vertices_add9(rbt_friend, vertices_user9): 
    if (rbt_friend.right):
        vertices_add9(rbt_friend.right, vertices_user9)
        
    for i in range(len(vertices_user9)):
        if(rbt_friend.id == vertices_user9[i]):
            for j in range(len(vertices_user9)):
                if(rbt_friend.friend_id == vertices_user9[j]):
                    v[i].add(v[j], 1)
                #    print(v[i], " 888 ",  vertices_user9[j])


    if (rbt_friend.left):
        vertices_add9(rbt_friend.left, vertices_user9)
        
    
def menu9():
    print("Find shortest path from a given user")

    global array_count9
    array_count9 = 0

    global vertices_user9
    global v

    vertices_user9 = [0 for i in range(user_number)]
    v = [0 for i in range(user_number)]

    array_init9(rbt_user.root)

    print("Input a start user id:")
    given_user = input()
    given_user_i = -1
    g = Dijkstra()
    for i in range(len(vertices_user9)):
        v[i] = g.add_vertex(vertices_user9[i])
        if vertices_user9[i] == int(given_user) :
            given_user_i = i

    if given_user_i == -1 :
        print("입력하신 user id 가 존재하지 않습니다.")
        return 0
        


        
    vertices_add9(rbt_friend.root, vertices_user9)


    v[given_user_i].d = 0

  #  given_user = 






#        p = self.vertices[n].first
 #       while p:
  #          print (p.n.name, end = ' ')

            
    
  #  g.print_vertices()
    g.shortest_path()
    g.print_vertices()
    
 #   add_friend(rbt_friend.root, v[0])
 #   vertices_add(rbt_friend.root, vertices_user9)

        


        

    
def main():
    while 1:
        menu_interface()
        menu_input = input()
        print(menu_input + "번을 선택하셨습니다.\n")
        menu_flag = 0

        if menu_input == "0":
            menu0()
        elif menu_input == "1":
            menu1()
        elif menu_input == "2":
            menu2()

        elif menu_input == "21":
            menu21()
            
        elif menu_input == "3":
            menu3()
        elif menu_input == "4":
            menu_flag = menu4()
        elif menu_input == "5":
            menu_flag = menu5()
        elif menu_input == "6":
            menu6()
        elif menu_input == "7":
            menu7()
        elif menu_input == "8":
            menu8()
        elif menu_input == "9":
            menu9()
        elif menu_input == "99":
            break

        if menu_flag != 0 :
            continue


        print("\n메뉴 인터페이스로 복귀하시려면 엔터 키를 누르세요")
        input()

        

main()
