#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from starlette.types import Receive, Scope, Send


class RemoteUserMiddleware:
    def __init__(self, asgi_app: Callable, remote_user: str) -> None:
        self.asgi_app = asgi_app
        self.remote_user = remote_user

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        scope["REMOTE_USER"] = self.remote_user
        await self.asgi_app(scope, receive, send)
