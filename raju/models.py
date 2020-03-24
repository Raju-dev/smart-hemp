from odoo import models, fields

class StudentRecord(models.Model):
    _name = "student.student"
    name = fields.Char(string='Name', required=True)
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    student_age = fields.Integer(string='Age')
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')

class MetrcPackage(models.Model):
    _name = "metrc.packages"
    label = fields.Char(string='Label')
    name = fields.Char(string='Name')
    metrc_id = fields.Integer(string='Metrc id', required=True)
    metrc_package_type = fields.Char(string='Metrc package type')
    metrc_room_id = fields.Integer(string='Age')
    metrc_packaged_date = fields.Date(string='Metrc packaged date')
    metrc_lab_testing_state = fields.Char(string='Metrc lab testing date') 
    metrc_lab_testing_state_date = fields.Date(string='Metrc packaged date')
    metrc_is_sample = fields.Integer(string='Metrc is sample')
    metrc_received_facility_license = fields.Char(string='Metrc recieved facility license')
    metrc_on_hold = fields.Integer(string='On hold')
    metrc_archieve_date = fields.Date(string='Metrc archived date')
    metrc_finished_date = fields.Date(string='Metrc finished date')
    metrc_item_id = fields.One2many('metrc.items', 'id')
    metrc_product_type_id = fields.Integer(string='Metrc product type id')
    metrc_unit_of_measure_name = fields.Char(string='Metrc unit of measure')
    user_id = fields.Integer(string='User id')

class MetrcRoom(models.Model):
    _name = "metrc.rooms"
    name = fields.Char(string='Metrc room name')
    metrc_id = fields.Integer(string='Metrc id')
    user_id = fields.Integer(string='User id')

class MetrcCategories(models.Model):
    _name = "metrc.categories"
    name = fields.Char(string='Metrc category name') 
    product_category_type = fields.Char(string='Category type') 
    quantity_type = fields.Char(string='Quantity type') 
    requires_strain = fields.Integer(string='Requires Strain', default = 0)
    requires_item_brand = fields.Integer(string='Requires Item Brand', default = 0)
    requires_administration_method = fields.Integer(string='Requires Administration Method', default = 0)
    requires_cbd_percent = fields.Integer(string='Requires CBD percent', default = 0)
    requires_cbd_content = fields.Integer(string='Requires CBD Content', default = 0)
    requires_thc_percent = fields.Integer(string='Requires THC Percent', default = 0)
    requires_thc_content = fields.Integer(string='Requires THC Content', default = 0)
    requires_unit_volume = fields.Integer(string='Requires unit volumne', default = 0)
    requires_unit_weight = fields.Integer(string='Requires unit weight', default = 0)
    requires_serving_size = fields.Integer(string='Requires serving size', default = 0)
    require_supply_duration_dates = fields.Integer(string='Requires supply duration dates', default = 0)
    requires_ingredients = fields.Integer(string='Requires ingredients', default = 0)
    requires_product_photo = fields.Integer(string='Requires product photo', default = 0)
    can_contain_seeds = fields.Integer(string='Can contain seeds', default = 0)
    can_be_remediated = fields.Integer(string='Can be remediated', default = 0)
    user_id = fields.Integer(string='User id', default = 0)
    
    display_name = fields.Char(string='Quantity type')

class MetrcStrains(models.Model):
    _name = "metrc.strains"
    name = fields.Char(string='Name') 
    thc_level = fields.Char(string='Metrc lab testing date') 
    cbd_level = fields.Char(string='Metrc lab testing date') 
    indica = fields.Char(string='Metrc lab testing date') 
    sativa = fields.Char(string='Metrc lab testing date') 
    genetics = fields.Char(string='Metrc lab testing date') 
    metrc_id = fields.Integer(string='Metrc id')
    test_status = fields.Char(string='Test Status')

class MetrcItems(models.Model):
    _name = "metrc.items"
    name = fields.Char(string='Metrc item name') 
    product_category_name = fields.Char(string='Metrc product category') 
    product_category_type = fields.Char(string='Metrc product category type') 
    quantity_type = fields.Char(string='Quantity type') 
    default_lab_testing_state = fields.Char(string='Default lab testing state') 
    unit_of_measure_name = fields.Char(string='Unit measure name') 
    approval_state = fields.Char(string='Approval state') 
    strain_id = fields.Integer(string='Strain id')
    strain_name = fields.Char(string='Strain name') 
    administration_method = fields.Char(string='Adminitration method') 
    cbd_percent = fields.Char(string='CBD percent') 
    cbd_content = fields.Char(string='CBD content') 
    cbd_unit_measure = fields.Char(string='CBD unit measure')
    thc_percent = fields.Char(string='THC percent')
    thc_content = fields.Char(string='THC content')
    thc_unit_measure = fields.Char(string='THC unit measure')
    unit_volume = fields.Char(string='THC unit volume')
    volume_unit_measure = fields.Char(string='Volume unit measure')
    unit_weight = fields.Char(string='Unit weight')
    weight_unit_measure = fields.Char(string='Weight unit measure')
    serving_size = fields.Char(string='Serving size')
    supply_duration_days = fields.Char(string='Supply duration days')
    unit_quantity = fields.Char(string='Unit quantity')
    quantity_unit_measure = fields.Char(string='Quantity unit measure')
    ingredients = fields.Char(string='Ingredients')
    user_id = fields.Integer(string='User id')
    metrc_id = fields.Integer(string='Metrc id')
    metrc_category_id = fields.Integer(string='Metrc category id')

class MetrcUnits(models.Model):
    _name = "metrc.units"
    name = fields.Char(string='Metrc units name')
    abbreviation = fields.Char(string='Metrc abbreviation')
    quantity_type = fields.Char(string='Metrc quantity type')

class MetrcTransfers(models.Model):
    _name = "metrc.transfers"
    metrc_id = fields.Integer(string='Metrc id')
    manifest_number = fields.Char(string='Manifest number')
    shipment_license_type = fields.Char(string='Shipment license type')
    shipper_facility_license_number = fields.Char(string='Facility license number')
    shipper_facility_name = fields.Char(string='Shipper facility name')
    name = fields.Char(string='Name')
    transporter_facility_license_number = fields.Char(string='Transporter facility license number')
    transporter_facility_name = fields.Char(string='Transporter facility name')
    driver_name = fields.Char(string='Driver name')
    driver_occupational_license_number = fields.Char(string='Driver occupational license number')
    driver_vehicle_license_number = fields.Char(string='Driver vehicle license number')
    vehicle_make = fields.Char(string='Vehicle make')
    vehicle_model = fields.Char(string='Vehicle model')
    vehicle_license_plate_number = fields.Char(string='Vehicle license plate number')
    delivery_count = fields.Integer(string='Delivery count')
    received_delivery_count = fields.Integer(string='Received delivery count')
    package_count = fields.Integer(string='Package count')
    received_package_count = fields.Integer(string='Received package count')
    contains_plant_package = fields.Integer(string='Contains plant package')
    contains_product_package = fields.Integer(string='Contains product package')
    contains_testing_sample = fields.Integer(string='Contains testing sample')
    contains_product_requires_remediation = fields.Integer(string='Contains product requires remediation')
    contains_remediated_product_package = fields.Integer(string='Contains remediated product package')
    created_date_time = fields.Date(string='Created date time')
    created_by_user_name = fields.Char(string='Created by user name')
    last_modified = fields.Date(string='Last modified ')
    delivery_id = fields.Integer(string='Delivery id')
    recipient_facility_license_number = fields.Char(string='Recipient facility license number')
    recipient_facility_name = fields.Char(string='Recipient facility name')
    shipment_type_name = fields.Char(string='Shipment type name')
    shipment_transaction_type = fields.Char(string='Shipment transaction type')
    estimated_departure_date_time = fields.Date(string='Estimated departure date time')
    actual_departure_date_time = fields.Date(string='Actual departure date time')
    estimated_arrival_date_time = fields.Date(string='Estimated arrival date time = ')
    actual_arrival_date_time = fields.Date(string='Actual arrival date time')
    delivery_package_count = fields.Integer(string='Delivery package count')
    delivery_received_package_count = fields.Integer(string='Delivery received package count')
    received_date_time = fields.Date(string='Received date time')
    user_id = fields.Integer(string='User id')