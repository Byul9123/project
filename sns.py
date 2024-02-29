class Member():
    name = " "
    username = " "
    password = " "

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")
        pass

    def __repr__(self):
        return f"{self.name}, {self.username}"


class Post():
    title = " "
    contant = " "
    author = " "
    def __init__(self, title, contant, author):
        self.title = title
        self.contant = contant
        self.author = author

    def __repr__(self):
        return f"아이디: {self.author}, 제목: {self.title}, 내용: {self.contant} "


members = []
user1 = Member('이한별', 'id1', 'asdlfjlas')
members.append(user1)
user2 = Member('이태성', 'id2', 'asdfhjk')
members.append(user2)
user3 = Member('이초아', 'id3', 'ajlkgsad')
members.append(user3)
# user1.display()
# user2.display()
# user3.display()


posts = []
post1 = Post('오늘의 맛집1', '등갈비', 'id1')
posts.append(post1)
post2 = Post('오늘의 맛집2', '돼지갈비', 'id1')
posts.append(post2)
post3 = Post('오늘의 맛집3', '양꼬치', 'id1')
posts.append(post3)
post4 = Post('최애 선수1', '박지성', 'id2')
posts.append(post4)
post5 = Post('최애 선수2', '손흥민', 'id2')
posts.append(post5)
post6 = Post('최애 선수3', '황희찬', 'id2')
posts.append(post6)
post7 = Post('하루 한마디1', '개을러지지말자', 'id3')
posts.append(post7)
post8 = Post('하루 한마디2', '미루지말자', 'id3')
posts.append(post8)
post9 = Post('하루 한마디3', '천천히 그때그때', 'id3')
posts.append(post9)


# print(members)
# print(posts)

for i in members:
    print(i.name)



for i in posts:
    if i.author == 'id2':
        print(i.title)


search = '비'
for i in posts:
    if search in i.contant:
        print(i.title)

while True:
    newmamber = input("새로운 맴버를 추가하시겠습니까? [Y/N]")
    if newmamber.lower() == 'y':
        print("이름을 입력하세요 : ")
        new_name = input()
        print("아이디를 입력하세요 : ")
        new_username = input()
        print("비밀번호를 입력하세요 : ")
        new_password = input()
        members.append(Member(new_name, new_username, new_password))
        print("새로운 멤버가 생성되었습니다!")
        continue
    elif newmamber.lower() == 'n':
        for i in members:
            i.display()
        break
    else:
        print("y / n 중 하나만 입력해주세요")
        continue

while True:
    new_post = input("포스팅 하시겠습니까? [Y/N]?")
    if new_post.lower() == 'y':
        print('제목을 입력하세요: ')
        new_title = input()
        print('내용을 입력하세요: ')
        new_contant = input()
        print('아이디를 입력하세요: ')
        new_author = input()
        posts.append(Post(new_title, new_contant, new_author))
        print('포스트가 등록되었습니다.')
        continue
    elif new_post.lower() == 'n':
            break
    else:
        print('잘못 입력하셨습니다 다시입력해 주세요')
        continue