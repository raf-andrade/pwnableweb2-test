# Copyright 2014 David Tomaschik <david@systemoverlord.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pwnableapp
import hashlib


app = pwnableapp.Flask('pwncart')
app.config.from_object('pwncart.config')
app.init_logging()

# CTF Flags
flags = {
    'free_cart': 'free_as_in_b33r',
    'account_credit': 'some_cash_machine_in_bumsville_idaho',
}
get_flag = flags.get
