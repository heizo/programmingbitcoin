# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper
import script
import tx
# -

# ### Exercise 1
#
# Write the version parsing part of the `parse` method that we've defined. To do this properly, you'll have to convert 4 bytes into a Little-Endian integer.
#
# #### Make [this test](/edit/code-ch05/tx.py) pass: `tx.py:TxTest:test_parse_version`

# +
# Exercise 1

reload(tx)
run(tx.TxTest("test_parse_version"))
# -

from io import BytesIO
from script import Script
script_hex = ('6b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278a')
stream = BytesIO(bytes.fromhex(script_hex))
script_sig = Script.parse(stream)
print(script_sig)

# ### Exercise 2
#
# Write the inputs parsing part of the `parse` method in `Tx` and the `parse` method for `TxIn`.
#
# #### Make [this test](/edit/code-ch05/tx.py) pass: `tx.py:TxTest:test_parse_inputs`

# +
# Exercise 2

reload(tx)
run(tx.TxTest("test_parse_inputs"))
# -

# ### Exercise 3
#
# Write the outputs parsing part of the `parse` method in `Tx` and the `parse` method for `TxOut`.
#
# #### Make [this test](/edit/code-ch05/tx.py) pass: `tx.py:TxTest:test_parse_outputs`

# +
# Exercise 3

reload(tx)
run(tx.TxTest("test_parse_outputs"))
# -

# ### Exercise 4
#
# Write the Locktime parsing part of the `parse` method in `Tx`.
#
# #### Make [this test](/edit/code-ch05/tx.py) pass: `tx.py:TxTest:test_parse_locktime`

# +
# Exercise 4

reload(tx)
run(tx.TxTest("test_parse_locktime"))
# -

# ### Exercise 5
#
# What is the ScriptSig from the second input, ScriptPubKey from the first output and the amount of the second output for this transaction?
#
# ```
# 010000000456919960ac691763688d3d3bcea9ad6ecaf875df5339e148a1fc61c6ed7a069e0100
# 00006a47304402204585bcdef85e6b1c6af5c2669d4830ff86e42dd205c0e089bc2a821657e951
# c002201024a10366077f87d6bce1f7100ad8cfa8a064b39d4e8fe4ea13a7b71aa8180f012102f0
# da57e85eec2934a82a585ea337ce2f4998b50ae699dd79f5880e253dafafb7feffffffeb8f51f4
# 038dc17e6313cf831d4f02281c2a468bde0fafd37f1bf882729e7fd3000000006a473044022078
# 99531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc26125022008b422690b84
# 61cb52c3cc30330b23d574351872b7c361e9aae3649071c1a7160121035d5c93d9ac96881f19ba
# 1f686f15f009ded7c62efe85a872e6a19b43c15a2937feffffff567bf40595119d1bb8a3037c35
# 6efd56170b64cbcc160fb028fa10704b45d775000000006a47304402204c7c7818424c7f7911da
# 6cddc59655a70af1cb5eaf17c69dadbfc74ffa0b662f02207599e08bc8023693ad4e9527dc42c3
# 4210f7a7d1d1ddfc8492b654a11e7620a0012102158b46fbdff65d0172b7989aec8850aa0dae49
# abfb84c81ae6e5b251a58ace5cfeffffffd63a5e6c16e620f86f375925b21cabaf736c779f88fd
# 04dcad51d26690f7f345010000006a47304402200633ea0d3314bea0d95b3cd8dadb2ef79ea833
# 1ffe1e61f762c0f6daea0fabde022029f23b3e9c30f080446150b23852028751635dcee2be669c
# 2a1686a4b5edf304012103ffd6f4a67e94aba353a00882e563ff2722eb4cff0ad6006e86ee20df
# e7520d55feffffff0251430f00000000001976a914ab0c0b2e98b1ab6dbf67d4750b0a56244948
# a87988ac005a6202000000001976a9143c82d7df364eb6c75be8c80df2b3eda8db57397088ac46
# 430600
# ```

# +
# Exercise 5

from io import BytesIO
from tx import Tx

hex_transaction = '010000000456919960ac691763688d3d3bcea9ad6ecaf875df5339e148a1fc61c6ed7a069e010000006a47304402204585bcdef85e6b1c6af5c2669d4830ff86e42dd205c0e089bc2a821657e951c002201024a10366077f87d6bce1f7100ad8cfa8a064b39d4e8fe4ea13a7b71aa8180f012102f0da57e85eec2934a82a585ea337ce2f4998b50ae699dd79f5880e253dafafb7feffffffeb8f51f4038dc17e6313cf831d4f02281c2a468bde0fafd37f1bf882729e7fd3000000006a47304402207899531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc26125022008b422690b8461cb52c3cc30330b23d574351872b7c361e9aae3649071c1a7160121035d5c93d9ac96881f19ba1f686f15f009ded7c62efe85a872e6a19b43c15a2937feffffff567bf40595119d1bb8a3037c356efd56170b64cbcc160fb028fa10704b45d775000000006a47304402204c7c7818424c7f7911da6cddc59655a70af1cb5eaf17c69dadbfc74ffa0b662f02207599e08bc8023693ad4e9527dc42c34210f7a7d1d1ddfc8492b654a11e7620a0012102158b46fbdff65d0172b7989aec8850aa0dae49abfb84c81ae6e5b251a58ace5cfeffffffd63a5e6c16e620f86f375925b21cabaf736c779f88fd04dcad51d26690f7f345010000006a47304402200633ea0d3314bea0d95b3cd8dadb2ef79ea8331ffe1e61f762c0f6daea0fabde022029f23b3e9c30f080446150b23852028751635dcee2be669c2a1686a4b5edf304012103ffd6f4a67e94aba353a00882e563ff2722eb4cff0ad6006e86ee20dfe7520d55feffffff0251430f00000000001976a914ab0c0b2e98b1ab6dbf67d4750b0a56244948a87988ac005a6202000000001976a9143c82d7df364eb6c75be8c80df2b3eda8db57397088ac46430600'

# convert the hex_transaction to binary
# create a stream using BytesIO
# use Tx.parse to get the transaction object.
# ScriptSig from second input
# ScriptPubKey from first output
# Amount from second output
stream = BytesIO(bytes.fromhex(hex_transaction))
tx_obj = Tx.parse(stream)
print(tx_obj.tx_ins[1].script_sig)
print(tx_obj.tx_outs[0].script_pubkey)
print(tx_obj.tx_outs[1].amount)
# -

# ### Exercise 6
#
# Write the `fee` method for the `Tx` class.
#
# #### Make [this test](/edit/code-ch05/tx.py) pass: `tx.py:TxTest:test_fee`

# +
# Exercise 6

reload(tx)
run(tx.TxTest("test_fee"))
# -


