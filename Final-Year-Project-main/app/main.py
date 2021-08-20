from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles


class SpaStaticFiles(StaticFiles): #Staticfiles for single-page-apps
    async def lookup_path(self, path): 
        full_path, stat_result = await super().lookup_path(path)
        if stat_result is None:
            return await super().lookup_path('./index.html')
        return full_path, stat_result

route = [
    Mount('', app=SpaStaticFiles(directory='www', html=True), name='frontend'),
]

app = Starlette(routes=route)

#starlette==0.16.0