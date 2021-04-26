from flask import *

app = Flask(__name__)


@app.route('/')
def mainpage():
    return """
        <!doctype html>
        <html>
            <head>
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                <title>Флеш игры</title>
            </head>
            <body>
                <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert">
                    <h4>
                        Добро пожаловать на сайт с самыми лучшими флеш играми!
                    <h4>
                    <h5>Здесь ты можешь найти любую игру, от трудной головоломки, до забавной, расслабляющей игры.<h5>  
                </div>
                <div class="container">
                    <div class="block">
                        <a href="/evo_city_driving" style="color: black">
                            <img src="/static/imgs/evo_city_driving.jpg" width="180px" height="135px">
                            <h5>EVO City Driving</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/truck_loader_5" style="color: black">
                            <img src="/static/imgs/truck_loader_5.jpg" width="180px" height="135px">
                            <h5>Truck Loader 5</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/lucky_toss_3d" style="color: black">
                            <img src="/static/imgs/lucky_toss_3d.jpg" width="180px" height="135px">
                            <h5>Lucky Toss 3D</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/car_destroy_car" style="color: black">
                            <img src="/static/imgs/car_destroy_car.jpg" width="180px" height="135px">
                            <h5>Car Destroy Car</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/puppet_soccer" style="color: black">
                            <img src="/static/imgs/puppet_soccer.jpg" width="180px" height="135px">
                            <h5>Puppet Soccer</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/5_minibattles" style="color: black">
                            <img src="/static/imgs/5_minibattles.jpg" width="180px" height="135px">
                            <h5>5 MiniBattles</h5>
                        </a>
                    </div>
                </div>
                <div class="container">
                    <div class="block">
                        <a href="/extreme_drift" style="color: black">
                            <img src="/static/imgs/extreme_drift.jpg" width="180px" height="135px">
                            <h5>Extreme Drift</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/brick_breaker" style="color: black">
                            <img src="/static/imgs/brick_breaker.jpg" width="180px" height="135px">
                            <h5>Brick Breaker</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/truck_parking_3d" style="color: black">
                            <img src="/static/imgs/truck_parking_3d.jpg" width="180px" height="135px">
                            <h5>Truck Parking 3D</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/archery" style="color: black">
                            <img src="/static/imgs/archery.jpg" width="180px" height="135px">
                            <h5>Archery</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/aircraft_simulator" style="color: black">
                            <img src="/static/imgs/aircraft_simulator.jpg" width="180px" height="135px">
                            <h5>Aircraft Simulator</h5>
                        </a>
                    </div>
                    <div class="block">
                        <a href="/march_madness" style="color: black">
                            <img src="/static/imgs/march_madness.jpg" width="180px" height="135px">
                            <h5>March Madness</h5>
                        </a>
                    </div>
                </div>
            </body>
        </html>
    """


@app.route('/evo_city_driving')
def evo_city_driving():
    return """
        <!doctype html>
        <html>
            <head>
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                <title>EVO City Driving</title>
            </head>
            <body>
                
                <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                    <h5>
                        <a href="/" style="color: white">Главная страница</a>
                    </h5>
                </div>
                <iframe
                    src="https://html5.gamemonetize.com/3s54ez6wyfvgu3cg52w86w08lsh25fk8/" 
                    width="1879" height="890" scrolling="none" frameborder="0">
                </iframe>
            </body>
        </html>  
    """


@app.route("/truck_loader_5")
def truck_loader_5():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Truck Loader 5</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/uoqfs8gs2redrwzbfo3diixqpd986v71/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/lucky_toss_3d")
def lucky_toss_3d():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Lucky Toss 3D</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/tycf4c0m00itmqfkot9sjlm3z67orwul/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/car_destroy_car")
def car_destroy_car():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Car Destroy Car</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/w5gxaf1jw48x630kz7nu5ua1tfub18sx/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/puppet_soccer")
def puppet_soccer():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Puppet Soccer</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/36tlng83d7y4zqhjrcsxc23bvip3r7xv/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/5_minibattles")
def five_minibattles():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>5 MiniBattles</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/yrgagn319t1pr7ief6nvie1esnnh5o93/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/extreme_drift")
def extreme_drift():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Extreme Drift</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/ezaupt4iwn8o12h87x0nvd2tr7ej6jyk/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/brick_breaker")
def brick_breaker():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Brick Breaker</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/4megg3ety7h6jcpk0us25akssli418o5/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/truck_parking_3d")
def truck_parking_3d():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Truck Parking 3D</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/hfvy5h3dlnj8w9ec0vtqezc6i7s9rqd9/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/archery")
def archery():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Archery</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/o0r5zqlrk5g8xf3gfhx7arsv6fj5zbvo/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


@app.route("/aircraft_simulator")
def aircraft_simulator():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>Aircraft Simulator</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/9iuuq6428a1ug5ro9zvm7iskwwe9ibbs/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """

@app.route("/march_madness")
def march_madness():
    return """
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="icon" href="/static/favicon/favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                    <title>March Madness</title>
                </head>
                <body>

                    <div class="p-3 mb-2 bg-primary text-white" class ="alert alert-primary" role="alert" >
                        <h5>
                            <a href="/" style="color: white">Главная страница</a>
                        </h5>
                    </div>
                    <iframe
                        src="https://html5.gamemonetize.com/114olmnx2sug8fd38ykp54las0cod3af/" 
                        width="1879" height="890" scrolling="none" frameborder="0">
                    </iframe>
                </body>
            </html>  
        """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
