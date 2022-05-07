import pytest 

from wallet import Wallet, InsufficientAmount, NegativeAmount 


def test_default_initial_amount(): 
  wallet = Wallet(10) 
  assert wallet.balance == 0 

  
def test_setting_initial_amount(): 
  wallet = Wallet(100) 
  assert wallet.balance == 100 

def test_wallet_add_cash(): 
  wallet = Wallet(10) 
  wallet.add_cash(-80) 
  assert wallet.balance == -70 

def test_wallet_add_cash(): 
  wallet = Wallet(10) 
  with pytest.raises(NegativeAmount): 
    wallet.add_cash(-80) 
  
def test_wallet_spend_cash(): 
  wallet = Wallet(20) 
  wallet.spend_cash(10) 
  assert wallet.balance == 10 

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(): 
  wallet = Wallet() 
  wallet.spend_cash(100) 
