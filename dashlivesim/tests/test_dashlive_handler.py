# The copyright in this software is being made available under the BSD License,
# included below. This software may be subject to other third party and contributor
# rights, including patent rights, and no such rights are granted under this license.
#
# Copyright (c) 2015, Dash Industry Forum.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#  * Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation and/or
#  other materials provided with the distribution.
#  * Neither the name of Dash Industry Forum nor the names of its
#  contributors may be used to endorse or promote products derived from this software
#  without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS AS IS AND ANY
#  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#  IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
#  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.

import unittest

from dashlivesim.mod_python import dashlive_handler

class TestRange(unittest.TestCase):
    "Test that ranges are handled correctly"

    def testDoubleRange(self):
        payload = "0123456789"
        rangeLine = "range=1-6"
        (pl, rangeResponse) = dashlive_handler.handle_byte_range(payload, rangeLine)
        self.assertEqual(pl, "123456", "Double range data not OK")
        self.assertEqual(rangeResponse, "bytes 1-6/10", "RangeResponse for double range")

    def testEndRange(self):
        payload = "0123456789"
        rangeLine = "range=1-"
        (pl, rangeResponse) = dashlive_handler.handle_byte_range(payload, rangeLine)
        self.assertEqual(pl, "123456789", "End Range payload")
        self.assertEqual(rangeResponse, "bytes 1-9/10", "RangeResponse for double range")

    def testLastRange(self):
        payload = "0123456789"
        rangeLine = "range=-6"
        (pl, rangeResponse) = dashlive_handler.handle_byte_range(payload, rangeLine)
        self.assertEqual(pl, "456789", "LastRange payload")
        self.assertEqual(rangeResponse, "bytes 4-9/10", "LastRange range")
