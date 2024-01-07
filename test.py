from faker import Faker
import pandas as pd

fake = Faker()



data = []
for _ in range(100):
    name = fake.name()
    email = fake.email()
    data.append([name, email])

df = pd.DataFrame(data, columns=['Name', 'Email'])

df.to_excel('fake_data.xlsx', index=False)






