# from django.http import response
# from rest_framework.test import APITestCase
# from django.test import SimpleTestCase
# from django.urls import reverse , resolve
# from rest_framework import status
# from django.db import IntegrityError
# from rest_framework.test import APIClient

# from Auth.models import User
# from tascrum.models import *
# from tascrum.views import CardView,CreateCardView,CardAssignmentView


# class cardTest(APITestCase, SimpleTestCase):
#     def test_CardView_url(self):
#         url = reverse("card-list")
#         self.assertEqual(resolve(url).func.cls, CardView)

#     def test_CardAssignmentView_url(self):
#         url = reverse("assign-list")
#         self.assertEqual(resolve(url).func.cls, CardAssignmentView)

#     def setUp(self):
#         self.client = APIClient()
#         user1 = User.objects.create_user(first_name='saba', last_name='razi',email='razi1.saba@gmail.com',\
#                                           username= "test username", password='thisissaba')
#         self.members = Member.objects.create(
#             user= user1,
#             occupations='Employee',
#             bio='Another test bio',
#             birthdate='1990-05-15'
#         )
#         self.workspace = Workspace.objects.create(name = 'workspace test2',type = 'small business', description = 'description test', backgroundImage = '')
#         self.board = Board.objects.create(
#             title='board test',
#             backgroundImage = "",
#             workspace=self.workspace
#         )
#         self.board.members.add(self.members)
#         self.list = List.objects.create(title='List test', board=self.board)
#         self.card = Card.objects.create(
#             title="card test",
#             list=self.list,
#             startdate='2022-05-15',
#             duedate='2024-05-15',
#             reminder='5 Minuets before',
#         )
#         self.card.members.add(self.members)
    
#     def authenticate(self):
#         register_data = {
#             'first_name':'test fname',
#             'last_name':'test lname',
#             'username': 'test username',
#             'email': 'fortest@gmail.com',
#             'password': 'Somepass',
#         }
#         response = self.client.post(reverse('user-list'), register_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         login_data = {
#             'email': 'fortest@gmail.com',
#             'password': 'Somepass',
#         }
#         response = self.client.post(reverse('jwt-create'), login_data)

#         self.assertTrue(response.status_code, status.HTTP_200_OK)
#         self.assertTrue(response.data["access"] is not None)

#         token = response.data["access"]
#         self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')

#     def test_card_fields(self):
#         self.assertEquals(self.card.title,'card test')
#         self.assertEquals(self.card.reminder,'5 Minuets before')
    
    

#     # def test_card_get_authenticated(self):
#     #     self.authenticate()
#     #     url = reverse('card-list') 
#     #     response = self.client.get(url)
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     return response

#     # def test_card_fields_after_get(self):
#     #     response = self.test_card_get_authenticated()
#     #     self.assertEquals(self.card.title,'card test')
#         # self.assertEquals(self.card.reminder,'5 Minuets before')

#     # def test_card_date_after_get(self):
#     #     response = self.test_card_get_authenticated()
#     #     self.assertEquals(self.card.duedate,'2024-05-15')
#     #     self.assertEquals(self.card.startdate,'2022-05-15')

#     def test_board_get_unauthenticated(self):
#         url = reverse('card-list') 
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         return response

# class CreateCardViewTest(APITestCase, SimpleTestCase):
#     def test_CreateCardView_url(self):
#         url = reverse("crcard-list")
#         self.assertEqual(resolve(url).func.cls, CreateCardView)
    
#     def setUp(self):
#         self.client = APIClient()
#         self.create_card_url = reverse('crcard-list')
#         user1 = User.objects.create_user(first_name='saba', last_name='razi',email='razi1.saba@gmail.com',\
#                                           username= "test username", password='thisissaba')
#         self.members = Member.objects.create(
#             user= user1,
#             occupations='Employee',
#             bio='Another test bio',
#             birthdate='1990-05-15'
#         )
#         self.workspace = Workspace.objects.create(name = 'workspace test2',type = 'small business', description = 'description test', backgroundImage = '')
#         self.board = Board.objects.create(
#             title='board test',
#             backgroundImage = "",
#             workspace=self.workspace
#         )
#         self.board.members.add(self.members)
#         self.list = List.objects.create(title='List test', board=self.board)
#         self.card = Card.objects.create(
#             title="card test",
#             list=self.list,
#             startdate='2022-05-15',
#             duedate='2024-05-15',
#             reminder='5 Days before',
#         )
#         self.card.members.add(self.members)

#     def authenticate(self):
#         register_data = {
#             'first_name':'test fname',
#             'last_name':'test lname',
#             'username': 'test username',
#             'email': 'fortest@gmail.com',
#             'password': 'Somepass',
#         }
#         response = self.client.post(reverse('user-list'), register_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         login_data = {
#             'email': 'fortest@gmail.com',
#             'password': 'Somepass',
#         }
#         response = self.client.post(reverse('jwt-create'), login_data)

#         self.assertTrue(response.status_code, status.HTTP_200_OK)
#         self.assertTrue(response.data["access"] is not None)

#         token = response.data["access"]
#         self.client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')
    
#     def test_Create_Card_POST(self):
#         self.authenticate()

#         create_card_data ={
#             'title':"card test",
#             'list':self.list.id,
#             'startdate':'2022-05-15',
#             'duedate':'2024-05-15',
#             'reminder':'5 Days before',
#         }

#             # Send a POST request to create a new workspace
#         resp = self.client.post(self.create_card_url, create_card_data)        
#         response=resp.json()
#         self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

#     # def test_Update_Card_PUT(self):
#     #     self.authenticate()

#     #     create_card_data ={
#     #         'title':"card test",
#     #         'list':self.list.id,
#     #         'startdate':'2022-05-15',
#     #         'duedate':'2024-05-15',
#     #         'reminder':'5 Days before',
#     #     }

#     #         # Send a POST request to create a new workspace
#     #     resp = self.client.post(self.create_card_url, create_card_data)        
#     #     response=resp.json()
#     #     print(response)
#     #     id=response['id']

#     #     data_update = {
#     #         'title':"card test change",
#     #         'list':self.list.id,
#     #         'startdate':'2022-05-15',
#     #         'duedate':'2024-05-15',
#     #         'reminder':'5 Minuets before',
#     #     }

#     #     url = reverse('crcard-detail', kwargs={'pk': id})
#     #     print(url)
#     #     resp = self.client.put(url, data_update)
#     #     print(resp.content)
#     #     self.assertEqual(resp.status_code, 200)


#     # def test_Delete_Board_DELETE(self):
#     #     self.authenticate()

#     #     create_board_data = {"title":'board test3', 'has_star':False,"backgroundImage":"", "workspace":self.workspace.id}

#     #         # Send a POST request to create a new workspace
#     #     resp = self.client.post(self.board_url, create_board_data)        
#     #     response=resp.json()
#     #     id=response['id']

#     #     url = reverse('crboard-detail', kwargs={'pk': id})
#     #     resp = self.client.delete(url)
#     #     self.assertEqual(resp.status_code,  status.HTTP_204_NO_CONTENT)
    

#     # def test_Create_Card_POST(self):
#     #     self.authenticate()
#     #     user1 = User.objects.create(first_name='saba', last_name='razi', email='razi1.saba@gmail.com',
#     #                                      username="test username", password='thisissaba')
#     #     self.members = Member.objects.create(
#     #         user=user1,
#     #         occupations='Employee',
#     #         bio='Another test bio',
#     #         birthdate='1990-05-15'
#     #     )
#     #     self.workspace = Workspace.objects.create(name='workspace test2', type='small business',
#     #                                               description='description test', backgroundImage='')
#     #     self.board = Board.objects.create(
#     #         title='board test',
#     #         backgroundImage="",
#     #         workspace=self.workspace
#     #     )

#     #     # Ensure Member is associated with the Board as an owner
#     #     # board_role = MemberBoardRole.objects.filter(member=self.members, board=self.board).first()
#     #     # if not board_role or board_role.role != "owner":
#     #     #     # Create MemberBoardRole if it doesn't exist or the role is not "owner"
#     #     #     board_role = MemberBoardRole.objects.create(member=self.members, board=self.board, role='owner')

#     #     self.list = List.objects.create(title='List test', board=self.board)

#     #     create_card_data = {
#     #         "title": "card 4 list 6",
#     #         "list": self.list.id,
#     #         "startdate": "2023-11-29T12:53:05.642000Z",
#     #         "duedate": "2023-11-27T11:13:51.230361Z",
#     #         "reminder": "At time of due date",
#     #         "storypoint": 0,
#     #         "setestimate": 0,
#     #         "description": "test",
#     #         "status": "pending"
#     #     }

#     #     # Assign the board_role to the card
#     #     # create_card_data["board_role"] = board_role.id

#     #     response = self.client.post(self.create_card_url, create_card_data, format='json')
#     #     print(response.content)

#     #     # Check if the response status code is 201 (Created)
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     #     # Optionally, you can check the response data for additional details
#     #     self.assertEqual(response.data['title'], 'card 4 list 6')

#     #     # Optionally, you can check if the new card is actually created in the database
#     #     new_card = Card.objects.get(title='card 4 list 6', list=self.list)
#     #     self.assertIsNotNone(new_card)

    
#     # def test_card_count(self):
#     #     self.authenticate()
#     #     card_data = {"title":"card test","list":"1","startdate":'2022-05-15',"duedate":'2024-05-15',"reminder":'1 Day before'}
#     #     response = self.client.post(reverse('crcard-list') , card_data)
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     #     card_data = {"title":"card test2","list":"1","startdate":'2022-05-15',"duedate":'2024-05-15',"reminder":'1 Day before'}
#     #     response = self.client.post(reverse('crcard-list') , card_data)
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
#     #     self.assertEqual(Card.objects.all().count(), 3)

#     #     self.assertEqual(Card.objects.filter(title='card test2').count(), 1)
