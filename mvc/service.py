class Model(object):

    service_map = {
        'email': {
            'number': 1000,
            'price': 2
        },
        'sms': {
            'number': 1000,
            'price': 10
        },
        'voice': {
            'number': 1000,
            'price': 15
        }
    }

class View(object):

    def list_services(self, services):
        for service in services:
            print 'service: {}'.format(service)

    def list_pricing(self, services):
        for service in services:
            print "For {} message you pay {}$".format(
                Model.service_map[service]['number'],
                Model.service_map[service]['price']
            )


class Controller(object):

    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.service_map.keys()
        return self.view.list_services(services)

    def get_priceing(self):
        services = self.model.service_map.keys()
        return self.view.list_pricing(services)

class Client(object):
    controller = Controller()
    print "Services provided: "
    controller.get_services()
    print "Pricing for services: "
    controller.get_priceing()
