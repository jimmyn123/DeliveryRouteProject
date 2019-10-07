# Jimmy Nguyen
# Student ID: 000579757

import constant


# class for the truck
class Truck:

    # initializes a new truck and sets defaults
    def __init__(self, truck_id, current_stop, package_count=0, distance_traveled=0.0,
                 distance_this_route=0.0, route_distance=0.0):
        self.packages = []
        self.truck_id = truck_id
        self.package_count = package_count
        self.distance_traveled = distance_traveled
        self.distance_this_route = distance_this_route
        self.route_distance = route_distance
        self.current_stop = current_stop
        self.hub = current_stop
        self.current_package = None

    # loads a package into the truck
    def load_package(self, package):
        # makes sure only 16 packages max and sets status
        if self.package_count < 16:
            self.packages.append(package)
            self.package_count += 1
            package.status = "in delivery"
            if package.id == 9:
                package.status = "wrong address, on truck"
            return True
        return False

    # unloads package of that id and other packages that had the same destination
    def unload_package(self, package_id, destination, current_time):
        for i in range(self.packages.__len__()-1, -1, -1):
            if self.packages[i].id == package_id or self.packages[i].destination == destination \
                    and self.packages[i].status == "in delivery":
                self.packages[i].status = "delivered at " + str(current_time)

                # resets the distances and removes the package
                self.distance_traveled += self.route_distance
                self.distance_this_route = 0.0
                self.route_distance = 0.0
                self.current_stop = self.packages[i].destination
                self.packages.remove(self.packages[i])
                self.package_count -= 1

    # picks the next package to deliver depending on time, then on distance
    def pick_next_package(self, route_map, current_time):
        if self.packages:
            current_package = self.packages[0]
            if current_package.status != "in delivery":
                current_package = None

            # find by closest destination
            for package in self.packages:
                if package.status == "in delivery":
                    if current_package is None or route_map.edge_weights[self.current_stop, package.destination] < \
                            route_map.edge_weights[self.current_stop, current_package.destination]:
                        current_package = package

            # picks package by earliest deadline first
            for package in self.packages:
                deliver_by = package.deliver_by
                if deliver_by:
                    if not current_package.deliver_by or deliver_by < current_package.deliver_by:
                        current_package = package

            # sets the route distance to the next stop
            if current_package:
                self.route_distance = route_map.edge_weights[self.current_stop, current_package.destination]
            else:
                self.route_distance = route_map.edge_weights[self.current_stop, self.hub]
            self.current_package = current_package
        else:
            self.current_package = None

    # gets the remaining capacity for the truck
    def get_available_slots(self):
        return 16-self.package_count

    # determine if the truck is full
    def is_full(self):
        return self.package_count == 16

    # delivers the actual package
    def deliver_package(self, route_map, current_time):
        # only triggers when the distance travel is enough to reach the destination
        if self.distance_this_route >= self.route_distance:
            if self.current_package:
                # unloads the package
                self.unload_package(self.current_package.id, self.current_package.destination, current_time)
            else:
                self.current_stop = self.hub
            # picks the next route
            self.pick_next_package(route_map, current_time)

        self.distance_this_route += constant.MILES_PER_MINUTE
