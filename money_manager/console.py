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
merchant_repo.save(merchant_1)
merchant_2 = Merchant("Lidl")
merchant_repo.save(merchant_2)
merchant_3 = Merchant("Odeon Cinemas")
merchant_repo.save(merchant_3)
merchant_4 = Merchant("Baked Pizza al Taglio")
merchant_repo.save(merchant_4)
merchant_5 = Merchant("EDF Energy")
merchant_repo.save(merchant_5)
merchant_6 = Merchant("Britannia Mortgage")
merchant_repo.save(merchant_6)
merchant_7 = Merchant("Esso Maryhill")
merchant_repo.save(merchant_7)

transaction_1 = Transaction(merchant_1, 32.50, tag_1)
transaction_repo.save(transaction_1)
transaction_2 = Transaction(merchant_2, 15.00, tag_1)
transaction_repo.save(transaction_2)
transaction_3 = Transaction(merchant_6, 420.00, tag_3)
transaction_repo.save(transaction_3)
transaction_4 = Transaction(merchant_3, 12.20, tag_2)
transaction_repo.save(transaction_4)
transaction_5 = Transaction(merchant_7, 35.00, tag_4)
transaction_repo.save(transaction_5)
transaction_6 = Transaction(merchant_5, 93.40, tag_3)
transaction_repo.save(transaction_6)
transaction_7 = Transaction(merchant_4, 12.60, tag_2)
transaction_repo.save(transaction_7)
    

pdb.set_trace()