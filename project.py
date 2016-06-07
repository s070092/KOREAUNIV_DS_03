class Vertex_User_Mentioned:
    def __init__(self):
        self.n = 0;
        self.id = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None
    def add(self, v):
        a = adj()
        a.n = v.n
        a.next = self.first
        self.first = a

class Int_Vertex_User_Mentioned(Vertex_User_Mentioned):
    def __init__(self):
        super().__init__()
        self.id = 0
    def less_than(self,other):
        return self.id < other.id
    def more_than(self,other):
        return self.id > other.id    
    def make_node(self,id):
        n = Int_Vertex_User_Mentioned()
        n.id = id  
        return n
    def print_node(self):
        print(self.id)

        



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
    def add(self, v):
        a = adj()
        a.n = v.n
        a.next = self.first
        self.first = a

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


class Vertex_Friend:
    def __init__(self):
        self.n = 0
        self.id = 0
        self.friend_id = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None

class Int_Vertex_Friend(Vertex_Friend):
    def __init__(self):
        super().__init__()
        self.id = 0
    def less_than(self,other):
        return self.id < other.id
    def make_node(self,id, friend_id):
        n = Int_Vertex_Friend()
        n.id = id
        n.friend_id = friend_id
        return n
    def print_node(self):
        print(self.id)
        


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
        print(self.word)



        
class Vertex_His_Her_Friend:
    def __init__(self):
        self.n = 0
        self.id = 0
        self.friend_id = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None

class Int_Vertex_His_Her_Friend(Vertex_Friend):
    def __init__(self):
        super().__init__()
        self.id = 0
    def less_than(self,other):
        return self.id < other.id
    def make_node(self,id, friend_id):
        n = Int_Vertex_His_Her_Friend()
        n.id = id
        n.friend_id = friend_id
        return n
    def print_node(self):
        print(self.id)


        
class Vertex_Mentioned_His_Her_Friend:
    def __init__(self):
        self.n = 0
        self.id = 0
        self.friend_id = 0
        self.first = None
        self.p = None
        self.left = None
        self.right = None

class Int_Vertex_Mentioned_His_Her_Friend(Vertex_Mentioned_His_Her_Friend):
    def __init__(self):
        super().__init__()
        self.id = 0
    def less_than(self,other):
        return self.id < other.id
    def more_than(self,other):
        return self.id > other.id    
    def make_node(self,id):
        n = Int_Vertex_Mentioned_His_Her_Friend()
        n.id = id
      #  n.friend_id = friend_id
        return n
    def print_node(self):
        print(self.id)



        

class BinarySearchTree:
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

    def insert_mentioned(self,z):
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
        elif z.more_than(y):
            y.right = z
            
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
    print("0. Read data files")
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
    
bst_user = BinarySearchTree()
bst_friend = BinarySearchTree()
bst_word = BinarySearchTree()
bst_user_mentioned = BinarySearchTree()
proto_user_mentioned = Int_Vertex_User_Mentioned()

bst_his_her_friend = BinarySearchTree()
bst_mentioned_his_her_friend = BinarySearchTree()
proto_mentioned_his_her_friend = Int_Vertex_Mentioned_His_Her_Friend()
    
def menu0():


    bst_user.__init__()
    bst_friend.__init__()
    bst_word.__init__()
    
    proto_user = Int_Vertex_User()

    user_file = open('user.txt')
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
            bst_user.insert(proto_user.make_node(temp_id, temp_date.replace('\n', ''), temp_name.replace('\n', '')))


    proto_friend = Int_Vertex_Friend()

    friend_file = open('friend.txt')
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
            bst_friend.insert(proto_friend.make_node(temp_id, temp_friend_id))



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
            bst_word.insert(proto_word.make_node(temp_id, temp_date.replace('\n', ''), temp_word.replace('\n', '')))

    print("Total users:", user_number)
    print("Total friendship records:", friend_number)
    print("Total tweets:", word_number)

    print("\n\n작업중.....\n")
    statistics_friend(bst_user.root, bst_friend.root)
    statistics_tweets(bst_user.root, bst_word.root)
    print("작업 완료\n")    
    return bst_user, bst_friend, bst_word





def statistics_friend_user(bst_user, bst_friend):
    if(bst_user.right):
        statistics_friend_user(bst_user.right, bst_friend)
    if(bst_user.id == bst_friend.id):
        bst_user.friend_count += 1
    if(bst_user.left):
        statistics_friend_user(bst_user.left, bst_friend)


def statistics_friend(bst_user, bst_friend):
    if (bst_friend.right):
        statistics_friend(bst_user, bst_friend.right)
    statistics_friend_user(bst_user, bst_friend)
    if (bst_friend.left):
        statistics_friend(bst_user, bst_friend.left)        

def statistics_friend_cal(bst_user, total_number, user_number, min_friend, max_friend):
    if (bst_user.right) :
        total_number, user_number, min_friend, max_friend = statistics_friend_cal(bst_user.right, total_number, user_number, min_friend, max_friend)
    total_number += bst_user.friend_count
    user_number += 1
    if bst_user.friend_count < min_friend :
        min_friend = bst_user.friend_count      
    if bst_user.friend_count > max_friend :
        max_friend = bst_user.friend_count      
    if (bst_user.left) :
        total_number, user_number, min_friend, max_friend = statistics_friend_cal(bst_user.left, total_number, user_number, min_friend, max_friend)

    return total_number, user_number, min_friend, max_friend


def statistics_tweets_cal(bst_user, total_tweet, tweet_count, min_tweet, max_tweet):
    if (bst_user.right) :
        total_tweet, tweet_count, min_tweet, max_tweet = statistics_tweets_cal(bst_user.right, total_tweet, tweet_count, min_tweet, max_tweet)
    total_tweet += bst_user.tweet_count
    tweet_count += 1
    if bst_user.tweet_count < min_tweet :
        min_tweet = bst_user.tweet_count      
    if bst_user.tweet_count > max_tweet :
        max_tweet = bst_user.tweet_count 
    if (bst_user.left) :
        total_tweet, tweet_count, min_tweet, max_tweet = statistics_tweets_cal(bst_user.left, total_tweet, tweet_count, min_tweet, max_tweet)

    return total_tweet, tweet_count, min_tweet, max_tweet


def statistics_tweets_user(bst_user, bst_word):
    if (bst_user.right):
        statistics_tweets_user(bst_user.right, bst_word)
    if(bst_user.id == bst_word.id):
        bst_user.tweet_count += 1
    if (bst_user.left):
        statistics_tweets_user(bst_user.left, bst_word)

def statistics_tweets(bst_user, bst_word):
    if (bst_word.right):
        statistics_tweets(bst_user, bst_word.right)
    statistics_tweets_user(bst_user, bst_word)    
    if (bst_word.left):
        statistics_tweets(bst_user, bst_word.left) 









def menu1():
    total_number = 0
    user_number = 0
    min_friend = 1E10    
    max_friend = 0

    total_tweet = 0
    tweet_count = 0
    min_tweet = 1E10
    max_tweet = 0

    total_number, user_number, min_friend, max_friend = statistics_friend_cal(bst_user.root, total_number, user_number, min_friend, max_friend) 
    print("Average number of friends:", total_number/user_number)
    print("Minimum number of friends:", min_friend)
    print("Maximum number of friends:", max_friend, "\n")

    total_tweet, tweet_count, min_tweet, max_tweet = statistics_tweets_cal(bst_user.root, total_tweet, tweet_count, min_tweet, max_tweet)
    print("Average tweets per user:", total_tweet/tweet_count)
    print("Minimum tweets per user:", min_tweet)
    print("Maximum tweets per user:", max_tweet)





       

def statistics_tweets_count(bst_word, bst_word1, most_word1, most_word1_count):
    if (bst_word.right):
        most_word1, most_word1_count = statistics_tweets_count(bst_word.right, bst_word1, most_word1, most_word1_count)

    if bst_word.word == bst_word1.word:
        bst_word1.word_count += 1
        if bst_word1.word_count > most_word1_count:
           most_word1 = bst_word1.word
           most_word1_count = bst_word1.word_count
    if (bst_word.left):
        most_word1, most_word1_count = statistics_tweets_count(bst_word.left, bst_word1, most_word1, most_word1_count)        
    return most_word1, most_word1_count



def statistics_tweets_count1(bst_word1, most_word1, most_word1_count):
    if (bst_word1.right):
        most_word1, most_word1_count = statistics_tweets_count1(bst_word1.right, most_word1, most_word1_count)
    most_word1, most_word1_count = statistics_tweets_count(bst_word.root, bst_word1, most_word1, most_word1_count)
    if (bst_word1.left):
        most_word1, most_word1_count = statistics_tweets_count1(bst_word1.left, most_word1, most_word1_count)   
    return  most_word1, most_word1_count

def statistics_tweets_count2(bst_word1, most_word1, most_word2, most_word2_count):
    if (bst_word1.right):
        most_word1, most_word2, most_word2_count = statistics_tweets_count2(bst_word1.right, most_word1, most_word2, most_word2_count)
    if most_word1 != bst_word1.word :
        most_word2, most_word2_count = statistics_tweets_count(bst_word.root, bst_word1, most_word2, most_word2_count)
    if (bst_word1.left):
        most_word1, most_word2, most_word2_count = statistics_tweets_count2(bst_word1.left, most_word1, most_word2, most_word2_count)   
    return  most_word1, most_word2, most_word2_count

def statistics_tweets_count3(bst_word1, most_word1, most_word2, most_word3, most_word3_count):
    if (bst_word1.right):
        most_word1, most_word2, most_word3, most_word3_count = statistics_tweets_count3(bst_word1.right, most_word1, most_word2, most_word3, most_word3_count)
    if ((most_word1 != bst_word1.word) and (most_word2 != bst_word1.word)) :
        most_word3, most_word3_count = statistics_tweets_count(bst_word.root, bst_word1, most_word3, most_word3_count)
    if (bst_word1.left):
        most_word1, most_word2, most_word3, most_word3_count = statistics_tweets_count3(bst_word1.left, most_word1, most_word2, most_word3, most_word3_count)   
    return  most_word1, most_word2, most_word3, most_word3_count

def statistics_tweets_count4(bst_word1, most_word1, most_word2, most_word3, most_word4, most_word4_count):
    if (bst_word1.right):
        most_word1, most_word2, most_word3, most_word4, most_word4_count = statistics_tweets_count4(bst_word1.right, most_word1, most_word2, most_word3, most_word4, most_word4_count)
    if ((most_word1 != bst_word1.word) and (most_word2 != bst_word1.word) and (most_word3 != bst_word1.word)) :
        most_word4, most_word4_count = statistics_tweets_count(bst_word.root, bst_word1, most_word4, most_word4_count)
    if (bst_word1.left):
        most_word1, most_word2, most_word3, most_word4, most_word4_count = statistics_tweets_count4(bst_word1.left, most_word1, most_word2, most_word3, most_word4, most_word4_count)   
    return  most_word1, most_word2, most_word3, most_word4, most_word4_count


def statistics_tweets_count5(bst_word1, most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count):
    if (bst_word1.right):
        most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count = statistics_tweets_count5(bst_word1.right, most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count)
    if ((most_word1 != bst_word1.word) and (most_word2 != bst_word1.word) and (most_word3 != bst_word1.word) and (most_word4 != bst_word1.word)) :
        most_word5, most_word5_count = statistics_tweets_count(bst_word.root, bst_word1, most_word5, most_word5_count)
    if (bst_word1.left):
        most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count = statistics_tweets_count5(bst_word1.left, most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count)   
    return  most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count

def bst_word_init(bst_word1):
    if (bst_word1.right):
        bst_word_init(bst_word1.right)
    bst_word1.word_count = 0
    bst_word1.user_count = 0
    if (bst_word1.left):
        bst_word_init(bst_word1.left)
    return bst_word1
        
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
    
    bst_word1 = bst_word
    most_word1, most_word1_count = statistics_tweets_count1(bst_word1.root, most_word1, most_word1_count)
    print("1:\t", most_word1, "\t", most_word1_count)
    bst_word1.root = bst_word_init(bst_word1.root)

    most_word1, most_word2, most_word2_count = statistics_tweets_count2(bst_word1.root, most_word1, most_word2, most_word2_count)
    print("2:\t", most_word2, "\t", most_word2_count)
    
    bst_word1.root = bst_word_init(bst_word1.root)    
    most_word1, most_word2, most_word3, most_word3_count = statistics_tweets_count3(bst_word1.root, most_word1, most_word2, most_word3, most_word3_count)
    print("3:\t", most_word3, "\t", most_word3_count)
    
    bst_word1.root = bst_word_init(bst_word1.root)
    most_word1, most_word2, most_word3, most_word4, most_word4_count = statistics_tweets_count4(bst_word1.root, most_word1, most_word2, most_word3, most_word4, most_word4_count)
    print("4:\t", most_word4, "\t", most_word4_count)
    
    bst_word1.root = bst_word_init(bst_word1.root)
    most_word1, most_word2, most_word3, most_word4, most_word5, most_word5_count = statistics_tweets_count5(bst_word1.root, most_word1, most_word2, most_word3, most_word4, most_word5_count, most_word5_count)
    print("5:\t", most_word5, "\t", most_word5_count) 






def statistics_tweets_user_count(bst_word, bst_word1, most_user1, most_user1_count):
    if (bst_word.right):
        most_user1, most_user1_count = statistics_tweets_user_count(bst_word.right, bst_word1, most_user1, most_user1_count)

    if bst_word.id == bst_word1.id:
        bst_word1.user_count += 1
        if bst_word1.user_count > most_user1_count:
           most_user1 = bst_word1.id
           most_user1_count = bst_word1.user_count

    if (bst_word.left):
        most_user1, most_user1_count = statistics_tweets_user_count(bst_word.left, bst_word1, most_user1, most_user1_count)        
    return most_user1, most_user1_count



def statistics_tweets_user_count1(bst_word1, most_user1, most_user1_count):
    if (bst_word1.right):
        most_user1, most_user1_count = statistics_tweets_user_count1(bst_word1.right, most_user1, most_user1_count)
    most_user1, most_user1_count = statistics_tweets_user_count(bst_word.root, bst_word1, most_user1, most_user1_count)
    if (bst_word1.left):
        most_user1, most_user1_count = statistics_tweets_user_count1(bst_word1.left, most_user1, most_user1_count)   
    return  most_user1, most_user1_count

def statistics_tweets_user_count2(bst_word1, most_user1, most_user2, most_user2_count):
    if (bst_word1.right):
        most_user1, most_user2, most_user2_count = statistics_tweets_user_count2(bst_word1.right, most_user1, most_user2, most_user2_count)
    if most_user1 != bst_word1.id :
        most_user2, most_user2_count = statistics_tweets_user_count(bst_word.root, bst_word1, most_user2, most_user2_count)
    if (bst_word1.left):
        most_user1, most_user2, most_user2_count = statistics_tweets_user_count2(bst_word1.left, most_user1, most_user2, most_user2_count)   
    return  most_user1, most_user2, most_user2_count

def statistics_tweets_user_count3(bst_word1, most_user1, most_user2, most_user3, most_user3_count):
    if (bst_word1.right):
        most_user1, most_user2, most_user3, most_user3_count = statistics_tweets_user_count3(bst_word1.right, most_user1, most_user2, most_user3, most_user3_count)
    if ((most_user1 != bst_word1.id) and (most_user2 != bst_word1.id)) :
        most_user3, most_user3_count = statistics_tweets_user_count(bst_word.root, bst_word1, most_user3, most_user3_count)
    if (bst_word1.left):
        most_user1, most_user2, most_user3, most_user3_count = statistics_tweets_user_count3(bst_word1.left, most_user1, most_user2, most_user3, most_user3_count)   
    return  most_user1, most_user2, most_user3, most_user3_count

def statistics_tweets_user_count4(bst_word1, most_user1, most_user2, most_user3, most_user4, most_user4_count):
    if (bst_word1.right):
        most_user1, most_user2, most_user3, most_user4, most_user4_count = statistics_tweets_user_count4(bst_word1.right, most_user1, most_user2, most_user3, most_user4, most_user4_count)
    if ((most_user1 != bst_word1.id) and (most_user2 != bst_word1.id) and (most_user3 != bst_word1.id)) :
        most_user4, most_user4_count = statistics_tweets_user_count(bst_word.root, bst_word1, most_user4, most_user4_count)
    if (bst_word1.left):
        most_user1, most_user2, most_user3, most_user4, most_user4_count = statistics_tweets_user_count4(bst_word1.left, most_user1, most_user2, most_user3, most_user4, most_user4_count)   
    return  most_user1, most_user2, most_user3, most_user4, most_user4_count    

def statistics_tweets_user_count5(bst_word1, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count):
    if (bst_word1.right):
        most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count = statistics_tweets_user_count5(bst_word1.right, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count)
    if ((most_user1 != bst_word1.id) and (most_user2 != bst_word1.id) and (most_user3 != bst_word1.id) and (most_user4 != bst_word1.id)) :
        most_user5, most_user5_count = statistics_tweets_user_count(bst_word.root, bst_word1, most_user5, most_user5_count)
    if (bst_word1.left):
        most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count = statistics_tweets_user_count5(bst_word1.left, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count)   
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
    
    bst_word1 = bst_word
    most_user1, most_user1_count = statistics_tweets_user_count1(bst_word1.root, most_user1, most_user1_count)
    print("1:\t", most_user1, "\t", most_user1_count)

    bst_word1.root = bst_word_init(bst_word1.root)
    most_user1, most_user2, most_user2_count = statistics_tweets_user_count2(bst_word1.root, most_user1, most_user2, most_user2_count)
    print("2:\t", most_user2, "\t", most_user2_count)

    bst_word1.root = bst_word_init(bst_word1.root)
    most_user1, most_user2, most_user3, most_user3_count = statistics_tweets_user_count3(bst_word1.root, most_user1, most_user2, most_user3, most_user3_count)
    print("3:\t", most_user3, "\t", most_user3_count)

    bst_word1.root = bst_word_init(bst_word1.root)
    most_user1, most_user2, most_user3, most_user4, most_user4_count = statistics_tweets_user_count4(bst_word1.root, most_user1, most_user2, most_user3, most_user4, most_user4_count)
    print("4:\t", most_user4, "\t", most_user4_count)

    bst_word1.root = bst_word_init(bst_word1.root)
    most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count = statistics_tweets_user_count5(bst_word1.root, most_user1, most_user2, most_user3, most_user4, most_user5, most_user5_count)
    print("5:\t", most_user5, "\t", most_user5_count)




class Adj_User:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.next = None
        self.first = None

        
    def add(self, id, name):
        self.id = id
        self.name = name
        self.next = self.first
    



def find_user_name2(bst_user, bst_word_id):
    if (bst_user.right):
        find_user_name(bst_user.right, bst_word_id)
    if bst_word_id == bst_user.id :
        print(bst_word_id, "\t", bst_user.name)        
    if (bst_user.left):
        find_user_name(bst_user.left, bst_word_id)

def find_user_name1(bst_user_mentioned_id):
    if (bst_user_mentioned_id.right):
        find_user_name1(bst_user_mentioned_id.right)
        
    print(bst_user_mentioned_id)

def find_user_name(bst_user_mentioned, bst_user):
    # print("888 ", bst_user_mentioned.id, bst_user.id)
    if (bst_user.right):
        find_user_name(bst_user_mentioned, bst_user.right)
   # find_user_name1(bst_user_mentioned.id)
   # print(bst_user_mentioned.id, bst_user.id)
    if (bst_user_mentioned.id == bst_user.id):
        print(bst_user_mentioned.id, bst_user.id)
    if (bst_user.left):
        find_user_name(bst_user_mentioned, bst_user.left)    


def find_user_mentioned(bst_word, tweeted_word):
    if (bst_word.right):
        find_user_mentioned(bst_word.right, tweeted_word)
    if tweeted_word == bst_word.word:
       # find_user_name(bst_user.root, bst_word.id)
       # print(bst_word.id, "\t", bst_word.word, "\t", bst_word.date)
        bst_user_mentioned.insert_mentioned(proto_user_mentioned.make_node(bst_word.id))


        
    if (bst_word.left):
        find_user_mentioned(bst_word.left, tweeted_word)
    return bst_word.id


def print_user_mentioned(bst_user_mentioned):
    if bst_user_mentioned == None :
        print("이 word를 mention하신 분이 안 계십니다.")
        return 1
    if (bst_user_mentioned.right):
        print_user_mentioned(bst_user_mentioned.right)
    print(bst_user_mentioned.id)
    if (bst_user_mentioned.left):
        print_user_mentioned(bst_user_mentioned.left)



def find_user_name(bst_user, bst_user_mentioned):
    if bst_user.id == int(bst_user_mentioned.id) :
        print(bst_user.id, bst_user.name)
    elif bst_user.id > int(bst_user_mentioned.id) :
        find_user_name(bst_user.left, bst_user_mentioned)
    else :
        find_user_name(bst_user.right, bst_user_mentioned)        

def find_user_mentioned_name(bst_user_mentioned):
    if (bst_user_mentioned.right):
        find_user_mentioned_name(bst_user_mentioned.right)
    find_user_name(bst_user.root, bst_user_mentioned)
    if (bst_user_mentioned.left):
        find_user_mentioned_name(bst_user_mentioned.left)
        
    
def menu4():
    bst_user_mentioned.__init__()
    print("Find users who tweeted a word")
    print("Input a word:")    
    tweeted_word = input()
    find_user_mentioned(bst_word.root, tweeted_word)
    absent = print_user_mentioned(bst_user_mentioned.root)
    if absent != 1 :
        print("\nname 도 확인하시려면 1번을 누르시고,")
        print("메뉴 인터페이스로 돌아가시려면 2번을 누르세요")
        print("입력하세요:")
        name_check = input()
        if name_check == "1":
            find_user_mentioned_name(bst_user_mentioned.root)
        else :
            return 1


def construct_mentioned_his_her_friend(bst_his_her_friend, bst_user_mentioned_id) :
    if (bst_his_her_friend.right):
        construct_mentioned_his_her_friend(bst_his_her_friend.right, bst_user_mentioned_id)
    if bst_his_her_friend.friend_id == bst_user_mentioned_id :
        bst_mentioned_his_her_friend.insert_mentioned(proto_mentioned_his_her_friend.make_node(bst_his_her_friend.id))
    if (bst_his_her_friend.left):
        construct_mentioned_his_her_friend(bst_his_her_friend.left, bst_user_mentioned_id)

def find_user_mentioned_friend(bst_user_mentioned):
    if (bst_user_mentioned.right):
        find_user_mentioned_friend(bst_user_mentioned.right)
    construct_mentioned_his_her_friend(bst_his_her_friend.root, bst_user_mentioned.id)
    if (bst_user_mentioned.left):
        find_user_mentioned_friend(bst_user_mentioned.left)


def print_mentioned_his_her_friend(bst_mentioned_his_her_friend):
    if bst_mentioned_his_her_friend == None :
        print("트위터 친구 분이 계시지 않습니다.")
        return 1
    if (bst_mentioned_his_her_friend.right):
        print_mentioned_his_her_friend(bst_mentioned_his_her_friend.right)
    print(bst_mentioned_his_her_friend.id)
    if (bst_mentioned_his_her_friend.left):
        print_mentioned_his_her_friend(bst_mentioned_his_her_friend.left)

def find_mentioned_his_her_friend_name(bst_mentioned_his_her_friend):
    if (bst_mentioned_his_her_friend.right):
        find_mentioned_his_her_friend_name(bst_mentioned_his_her_friend.right)
    find_user_name(bst_user.root, bst_mentioned_his_her_friend)
    if (bst_mentioned_his_her_friend.left):
        find_mentioned_his_her_friend_name(bst_mentioned_his_her_friend.left)
        
def menu5():
    bst_his_her_friend.__init__()
    bst_mentioned_his_her_friend.__init__()
    proto_his_her_friend = Int_Vertex_His_Her_Friend()
    proto_mentioned_his_her_friend = Int_Vertex_Mentioned_His_Her_Friend()

    friend_file = open('friend01.txt')
    line_count = -1
    for line in friend_file:
        line_count += 1
 
        if line_count%3 == 0 :
            temp_id = int(line)
        elif line_count%3 == 1 :
            temp_friend_id = int(line)
            bst_his_her_friend.insert(proto_his_her_friend.make_node(temp_friend_id, temp_id))
            if bst_user_mentioned.root == None :
                print("4번 메뉴를 먼저 이용하셔야 5번 메뉴 자료가 구축됩니다.")
                print("Find users who tweeted a word")
                return 1
    find_user_mentioned_friend(bst_user_mentioned.root)
    absent = print_mentioned_his_her_friend(bst_mentioned_his_her_friend.root)

    if absent != 1 :
        print("\nname 도 확인하시려면 1번을 누르시고,")
        print("메뉴 인터페이스로 돌아가시려면 2번을 누르세요")
        print("입력하세요:")
        name_check = input()
        if name_check == "1":
            find_mentioned_his_her_friend_name(bst_mentioned_his_her_friend.root)
        else :
            return 1

    
    # bst_mentioned_his_her_friend.print_tree()
    
    # bst_his_her_friend.print_tree()
     



    
def main():
    while 1:
        menu_interface()
        menu_input = input()
        print(menu_input + "번을 선택하셨습니다.\n")

        if menu_input == "0":
            menu0()
        elif menu_input == "1":
            menu1()
        elif menu_input == "2":
            menu2()
        elif menu_input == "3":
            menu3()
        elif menu_input == "4":
            menu4()
        elif menu_input == "5":
            menu5()
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


        print("\n메뉴 인터페이스로 돌아가시려면 엔터 키를 누르세요\n")
        input()

        

main()
