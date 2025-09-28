from app.models.models import Service, Inventory, PartUsage
from app import db
from datetime import datetime

class ServiceManager:
    @staticmethod
    def create_service(vehicle_id, service_type, description, appointment_date, technician_id=None):
        service = Service(
            vehicle_id=vehicle_id,
            service_type=service_type,
            description=description,
            appointment_date=appointment_date,
            technician_id=technician_id,
            status='scheduled'
        )
        db.session.add(service)
        db.session.commit()
        return service

    @staticmethod
    def update_service_status(service_id, status, completion_date=None):
        service = Service.query.get_or_404(service_id)
        service.status = status
        if status == 'completed' and completion_date:
            service.completion_date = completion_date
        db.session.commit()
        return service

    @staticmethod
    def assign_technician(service_id, technician_id):
        service = Service.query.get_or_404(service_id)
        service.technician_id = technician_id
        db.session.commit()
        return service

class InventoryManager:
    @staticmethod
    def add_inventory(name, part_number, description, quantity, price, reorder_level, supplier):
        inventory = Inventory(
            name=name,
            part_number=part_number,
            description=description,
            quantity=quantity,
            price=price,
            reorder_level=reorder_level,
            supplier=supplier
        )
        db.session.add(inventory)
        db.session.commit()
        return inventory

    @staticmethod
    def update_quantity(inventory_id, quantity_change):
        inventory = Inventory.query.get_or_404(inventory_id)
        inventory.quantity += quantity_change
        db.session.commit()
        return inventory

    @staticmethod
    def check_low_stock():
        return Inventory.query.filter(Inventory.quantity <= Inventory.reorder_level).all()

    @staticmethod
    def use_parts(service_id, parts_used):
        """
        parts_used: list of dictionaries containing inventory_id and quantity
        """
        total_cost = 0
        for part in parts_used:
            inventory = Inventory.query.get_or_404(part['inventory_id'])
            if inventory.quantity < part['quantity']:
                raise ValueError(f"Insufficient quantity for part {inventory.name}")
            
            part_usage = PartUsage(
                service_id=service_id,
                inventory_id=inventory.id,
                quantity=part['quantity'],
                unit_price=inventory.price
            )
            
            inventory.quantity -= part['quantity']
            total_cost += inventory.price * part['quantity']
            
            db.session.add(part_usage)
        
        service = Service.query.get_or_404(service_id)
        service.cost = total_cost
        db.session.commit()
        return total_cost