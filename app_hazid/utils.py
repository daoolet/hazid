def get_user_id(request):
    return request.user.id if request.user.is_authenticated else None


YES_NO_CHOICES = [
    (True, "Yes"),
    (False, "No"),
]

ACTIVITY_OBSERVED = [
    ("Lifting/Rigging", "Lifting/Rigging"),
    ("Piping", "Piping"),
    ("Electrical/Instrument", "Electrical/Instrument"),
    ("Hauling (Truck Operations)", "Hauling (Truck Operations)"),
    ("Scaffolding", "Scaffolding"),
    ("Refueling Operations", "Refueling Operations"),
    ("Inspection/Testing", "Inspection/Testing"),
    ("Insulation", "Insulation"),
    ("General Labor/Preservation", "General Labor/Preservation"),
    ("Blasting/Coating", "Blasting/Coating"),
    ("Carpentry", "Carpentry"),
    ("Welding Activity/Cutting", "Welding Activity/Cutting"),
    ("Structural Steel/Erection", "Structural Steel/Erection"),
    ("Concrete/Grout/Masonry", "Concrete/Grout/Masonry"),
    ("Office", "Office"),
]

I_OBSERVED = [
    ("Unsafe Condition", "Unsafe Condition"),
    ("Unsafe act", "Unsafe act"),
    ("Positive observation", "Positive observation"),
]

POSSIBLE_CONSEQUENCES = [
    ("Injury/Illness", "Injury/Illness"),
    ("Environmental damage/spill", "Environmental damage/spill"),
    ("Equipment/property damage/loss", "Equipment/property damage/loss"),
    ("Fire", "Fire"),
    ("Motor vehicle accident", "Motor vehicle accident"),
    ("Other", "Other"),
]

CONDITIONS_RELATED = [
    ("Barricade/hole cover", "Barricade/hole cover"),
    ("Confined space", "Confined space"),
    ("Crane/Rigging/Certifications/Plans", "Crane/Rigging/Certifications/Plans"),
    ("Energy isolation (LOTO)", "Energy isolation (LOTO)"),
    ("Excavation", "Excavation"),
    ("Slip/trip/fall", "Slip/trip/fall"),
    ("Fire", "Fire"),
    ("Housekeeping", "Housekeeping"),
    ("Hot work", "Hot work"),
    ("Work permits/PPHA/JSA", "Work permits/PPHA/JSA"),
    ("Spill", "Spill"),
    ("Dropped Object/Gravity", "Dropped Object/Gravity"),
    ("Respiratory", "Respiratory"),
    ("Human and machine interface (HMI)", "Human and machine interface (HMI)"),
    ("Ladder/work platform", "Ladder/work platform"),
    ("Working @ Heights", "Working @ Heights"),
    ("Material handling", "Material handling"),
    ("Motorized equipment/vehicle", "Motorized equipment/vehicle"),
    ("PPE", "PPE"),
    ("Procedure compliance", "Procedure compliance"),
    ("Manual Handling", "Manual Handling"),
    ("Tools/equipment", "Tools/equipment"),
    ("Pinch point/Line of fire", "Pinch point/Line of fire"),
    ("Winterization", "Winterization"),
    ("Lighting/Illumination", "Lighting/Illumination"),
    ("Hand protection", "Hand protection"),
]