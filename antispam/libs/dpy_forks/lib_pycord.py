"""
The MIT License (MIT)

Copyright (c) 2020-Current Skelmis

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import datetime
import logging


from antispam.libs.dpy_forks import BaseFork


import discord  # pycord


log = logging.getLogger(__name__)


class Pycord(BaseFork):
    def __init__(self, handler):
        self.handler = handler
        self.bot = self.handler.bot

        log.debug(
            "Support for this package is:\n"
            "1) Based on documentation\n"
            "2) Untested, both unittests and implementation tests\n"
            "3) Out of respect for the fact it gets a half decent amount of downloads, "
            "and is therefore likely used by my audience\n"
            "4) That's it. Got issues? Open a Github issue."
        )

    async def timeout_member(
        self, member: discord.Member, original_message, until: datetime.timedelta
    ) -> None:
        # This doesn't bother permissions checking because
        # I couldn't be bothered handling it nicely
        #
        # Will still work fine. I think.
        await member.timeout_for(
            duration=until, reason="Automated timeout from Discord-Anti-Spam"  # type: ignore
        )
