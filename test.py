from faker import Faker
import pandas as pd

fake = Faker()



data = []
for _ in range(100):
    name = fake.name()
    email = fake.email()
    address = fake.address()
    data.append([name, email , address])

df = pd.DataFrame(data, columns=['Name', 'Email','address'])

df.to_excel('fake_data_2.xlsx', index=False)






