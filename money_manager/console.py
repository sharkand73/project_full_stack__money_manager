import pdb

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo


transaction_repo.delete_all()
merchant_repo.delete_all()
tag_repo.delete_all()


tag_1 = Tag("Groceries")
tag_repo.save(tag_1)
tag_2 = Tag("Entertainment")
tag_repo.save(tag_2)
tag_3 = Tag("Direct Debit")
tag_repo.save(tag_3)
tag_4 = Tag("Petrol")
tag_repo.save(tag_4)
merchant_1 = Merchant("Tesco")

merchant_2 = Merchant("Lidl")

merchant_3 = Merchant("Odeon Cinemas")

merchant_4 = Merchant("Baked Pizza al Taglio")

merchant_5 = Merchant("EDF Energy")

merchant_6 = Merchant("Britannia Mortgage")

merchant_7 = Merchant("Esso Maryhill")

transaction_1 = Transaction(merchant_1, tag_1, 32.50)

transaction_2 = Transaction(merchant_2, tag_2, 15.00)

transaction_3 = Transaction(merchant_6, tag_3, 420.00)

transaction_4 = Transaction(merchant_2, tag_1, 12.20)

transaction_5 = Transaction(merchant_7, tag_4, 35.00)

transaction_6 = Transaction(merchant_5, tag_3, 93.40)

transaction_7 = Transaction(merchant_4, tag_2, 12.60)

    

pdb.set_trace()