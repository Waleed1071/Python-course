from faker import Faker
import pandas as pd

fake = Faker()



data = []
for _ in range(100):
    name = fake.name()
    email = fake.email()
    phone = fake.address()
    data.append([name, email , phone])

df = pd.DataFrame(data, columns=['Name', 'Email','Phone'])

df.to_excel('fake_data_2.xlsx', index=False)






