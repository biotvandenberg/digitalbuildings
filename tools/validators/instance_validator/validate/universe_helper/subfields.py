"""Sets up a minimal subfield universe required for testing."""

from yamlformat.validator import subfield_lib

SUBFIELD_FOLDER = subfield_lib.SubfieldFolder(folderpath='subfields')
SUBFIELD_UNIVERSE = subfield_lib.SubfieldUniverse(folders=[SUBFIELD_FOLDER])

SUBFIELD_FOLDER.AddFromConfig(
    config_filename='subfields/subfields.yaml',
    documents=[{
        'aggregation': {
            'average':
                'Average value (e.g. average_zone_air_temperature_sensor)',
            'max':
                'Maximum value (e.g. Max_Cooling_Air_Flow_Setpoint)',
            'min':
                'Minimum value (e.g. Min_Ventilation_Air_Flow_Setpoint)',
            'total':
                'Sum total of some set of values (e.g. total_request_heating_count)'
        },
        'component': {
            'battery':
                'A device used to store power for use at a later time (e.g. in an emergency where grid power is unavailable).',
            'cable':
                'A length of wire, sometimes shielded externally, used for some purpose (e.g. steel braided wire for tensile support, CAT5 cable for communications, etc.).',
            'coil':
                'Component that exchanges heat between two media streams.',
            'compressor':
                'Component which drives refrigerant compression (and thus cooling processes) within a device or system.',
            'condenser':
                'The component of a refrigeration system that condenses refrigerant.',
            'controller':
                'Control loop, such as a PID controller.',
            'cooler':
                'Device used to cool product (e.g. walk-in food cooler) or media.',
            'damper':
                'Component which meters the flow of air within a system or device.',
            'dehumidifier':
                'Device used to dehumidify air.',
            'device':
                'The core equipment being represented by the Field groupings.',
            'dial':
                'Adjustment device (e.g. setpoint dial).',
            'dimmer':
                "A device which can reduce lighting output of a lamp (thus 'dimming' the light).",
            'dishwasher':
                'Device that washes dishes.',
            'dryer':
                'A component used for drying clothes.',
            'evaporator':
                'The component of a refrigeration system that evaporates refrigerant.',
            'fan':
                'Component used for the distribution of air.',
            'filter':
                'Component used for removing dust and other particulate matter from the air.',
            'guidevane':
                'Control vanes that meter refrigerant (on a centrifugal chiller) or air (on an AHU).',
            'heater':
                'Component which provides heat to media.',
            'humidifier':
                'Component which humidifies.',
            'lamp':
                'The component of a lighting device that emits the light.',
            'pump':
                'Component used for the distribution of liquid media.',
            'shade':
                'Window covering.',
            'tank':
                'Storage device for media.',
            'valve':
                'Component which meters the flow of water within a system or device.',
            'vane':
                'Component for guiding media flow.',
            'wheel':
                'Component used for transfer of heat from incoming to outgoing air streams. '
        },
        'descriptor': {
            'air':
                'Atmospheric air, either conditioned or unconditioned',
            'aisle':
                'Passage between two rows of server racks.',
            'blowdown':
                'Process of expelling water filled with mineral deposits for the purposes of water treatment. ',
            'boost':
                'Component used to boost pressure.',
            'broken':
                'A state of disrepair; fractured or segmented.',
            'building':
                'Applies to the entire building or group of zones within building (e.g. Building_Air_Static_Pressure_Sensor)',
            'bypass':
                'Route which fluid takes to bypass process.',
            'calendar':
                'A system structured around the days, weeks, and the months, used to manage schedules.',
            'call':
                'An action of speaking or meeting among multiple people.',
            'chilled':
                'Cold water (typically 40 - 50F)',
            'circulation':
                'Process or component used to circulate fluid through a device or system (typically onboard a boiler).',
            'co':
                'Measures carbon monoxide concentration.',
            'co2':
                'Measures carbon dioxide concentration.',
            'cogeneration':
                'Associated with a cogeneration process.',
            'cold':
                'Associated with cold area or process.',
            'condensing':
                'Process of gaseous refrigerant changing to liquid.',
            'conference':
                'An instance of speaking or meeting among multiple people.',
            'control':
                'The process of governing the actions of a device.',
            'cooling':
                'Process, measured effect or requirement for cooling.',
            'dehumidification':
                'Process of removing moisture from air.',
            'detection':
                'Process of identifying conditions.',
            'discharge':
                'Media leaving system to enter ambient conditioned space. Typically applies only to air-side systems.',
            'east':
                'Cardinal direction; opposite of west',
            'economizer':
                'Process or component responsible for the utilization of free cooling.',
            'electric':
                'Process or component driven by electricity (as to distinguish from natural gas, for instance).',
            'email':
                'A unique identifier address in the Internet.',
            'emergency':
                'a situation that poses an immediate risk to health, life property,  or environment.',
            'entering':
                ' The process of going into a thing (e.g. entering a heat exchanger).',
            'evaporative':
                'Process associated with the evaporation of water.',
            'event':
                'A thing of occassion that happens.',
            'exchange':
                'the transfer of heat from one fluid stream to another.',
            'exercise':
                "Mode of running equipment to maintain functionality ('exercise mode')",
            'exhaust':
                'Process or component used in the removal of air from a conditioned system to the outside atmosphere.',
            'panel':
                'An interface to control a device.',
            'fabric':
                'Textile material.',
            'fire':
                'a potential to cause physical damage through burning',
            'flue':
                'Chimney for conveying exhaust gas.',
            'gas':
                'Process or component driven by natural gas (as to distinguish from electric).',
            'glycol':
                'Liquid mixture consisting of glycol and water ',
            'guide':
                'Component used to guide flow of media or movement of component.',
            'hash':
                'A computed value that is converted from an original value.',
            'heating':
                'Process, measured effect or requirement for heating.',
            'heat':
                'Quality of media indicating energy level.',
            'high':
                'Level of control or measurement; above medium and low; opposite of low.',
            'hot':
                'Associated with hot area or process.',
            'humidification':
                'Process of adding moisture to air.',
            'id':
                'An identification or identifier.',
            'inlet':
                'Area of media entrance.',
            'input':
                'The input to a system.',
            'inter':
                'Represents something in between references (e.g. average_inter_line_voltage, the average voltage between lines).',
            'isolation':
                'Process of isolating one component or process from another.',
            'leak':
                'Media leaving the system abnormally.',
            'leaving':
                'Area where media leaves process.',
            'limit':
                'A boundary condition for a control (e.g. low limit).',
            'line':
                'Refers to the incoming electrical feed (e.g. line current).',
            'loop':
                'Recirculating loop.',
            'low':
                'Level of control or measurement; below medium and high; opposite of high.',
            'makeup':
                'Process of adding ("making-up") water that has been lost due to blowdown or evaporation.',
            'manufacturer':
                'The company which produces the asset or device.',
            'matched':
                'A collection of things that are put together as being equal, similar, or complementary.',
            'master':
                'Highest priority (or primary control) device, sensor, etc.',
            'medium':
                'Level of control or measurement; between high and low.',
            'message':
                'A communication sent to or left for a recipient.',
            'mixed':
                'Process or component used to mix multiple streams of air.',
            'mixing':
                'Process of mixing substance.',
            'model':
                'Particular design version of an asset (e.g. model_label).',
            'neutral':
                'Line in the electrical cirucit which carries current back to the source. Distinct from ground.',
            'next':
                'Something that occurs directly in time after the present or most recent one.',
            'no2':
                'Nitrogen dioxide.',
            'north':
                'Cardinal direction; opposite of south',
            'occupancy':
                'State of being occupied.',
            'occupied':
                'State of being within scheduled (time of day or week) run-time parameters.',
            'ongoing':
                'Hapenning currently, right now.',
            'output':
                'The output of a control loop (e.g. PID Loop Output)',
            'particle':
                'A very fine clump of solid matter.',
            'outside':
                'Process or measurement of local atmospheric conditions.',
            'phase1':
                'The first (nominally A) phase of three-phase power distribution systems.',
            'phase2':
                'The second (nominally B) phase of three-phase power distribution systems.',
            'phase3':
                'The third (nominally C) phase of three-phase power distribution systems.',
            'photocatalyst':
                'a material that uses absorbed light energy (usually UV) to drive desired reactions that would not otherwise proceed under ambient conditions',
            'preheating':
                'Process of preheating.',
            'pressurization':
                'Relating to the level of pressure in a system or vessel.',
            'primary':
                'Associated with the primary (production) loop of a production process.',
            'process':
                'Act of processing.',
            'production':
                'The loop in a system that is responsible for the conditioning of fluid.',
            'program':
                'Embedded, encoded instructions for the automatic performance of a task; typically within a controller.',
            'protection':
                'Act of preventing damage to object.',
            'recovery':
                'Component or process used for the reclamation of heat.',
            'release':
                'To free from constraints (e.g. to release the door from its magnetic lock).',
            'refrigerant':
                'Substance used in the mechanical refrigeration process (e.g. R-134a)',
            'request':
                'A signal from a system device that calls for more of a particular conditioning process (e.g. pressure requests from terminal units).',
            'return':
                'Measurement or process of media as it is returned from the end-use equipment within the system.',
            'reversing':
                'Reverses direction of flow (e.g. reversing valve on heat pump).',
            'room':
                'A space that can be occupied, or a part or division of a building or floor enclosed by walls.',
            'scene':
                "The holistic ambience achieved from coordinated control of an area's lighting levels and colors. One of many stored setpoints that may be recalled to apply predetermined lighting levels across a number of fixtures.",
            'schedule':
                'Refers to the time-of-day run-time requirements for the equipment.',
            'season':
                'Weather conditions under which certain systems or processes are enabled.',
            'secondary':
                'Associated with the secondary (distribution) loop of a produciton process.',
            'seismic':
                'Related to seismic activity (such as seismic gas shutoff valves).',
            'side':
                'Position relative to an an object.',
            'smoke':
                'Visible, suspended particles created during a fire.',
            'source':
                'The upstream source of conditioning (used specifically for heat exchangers).',
            'south':
                'Cardinal direction; opposite of north',
            'southeast':
                'Inter-cardinal direction between South and East.',
            'southwest':
                'Inter-cardinal direction between South and West.',
            'spray':
                'Spray of water through air.',
            'stage':
                'Discrete step (stage) of device activity (such as heating and cooling outputs).',
            'steam':
                'Water in gaseous form.',
            'suction':
                'The production of a partial vacuum in order to force fluid into a vacant space (such as refrigerant in a compressor).',
            'summer':
                'Method or process used during warmer weather (i.e. summer season).',
            'supervisor':
                'A program that controls a device from a supervisory (i.e. remote or external) level.',
            'supply':
                'Measurement or process of media as it is supplied to the end-use equipment within the system.',
            'suppression':
                'a range of firefighting tactics used to suppress fire',
            'sweeper':
                'Action performed in a sump to prevent sediment build-up via water turbulence.',
            'sync':
                'The simultaneous operation or activity of two or more things.',
            'tertiary':
                'Associated with the tertiary (peripheral) loops of a production process.',
            'ultraviolet':
                'A short wavelength type of light that is beyond the visible spectrum. It is damaging to DNA and cells, and is commonly used to sterilize surfaces.',
            'unoccupied':
                'State of being outside of scheduled (time of day or week) run-time parameters.',
            'use':
                "A descriptor for how the entity in question is used (e.g. zone_use_label = 'office') ",
            'user':
                'A person who uses or operates something.',
            'ventilation':
                'Process used to provide fresh air into a system or zone. ',
            'voc':
                'Measures volatile organic component concentration.',
            'water':
                'Water in liquid form, conditioned or unconditioned',
            'west':
                'Cardinal direction; opposite of east',
            'wind':
                'Movement of ambient air.',
            'winter':
                'Method or process used during colder weather (i.e. winter season).',
            'zone':
                'Region of building which is conditioned.'
        },
        'measurement': {
            'concentration':
                'Concentration of chemical (usually in parts per million or parts per billion).',
            'current':
                'Flow of electric charge.',
            'energy':
                ' The quantitative property that must be transferred to an object to perform work (default electrical unless otherwise modified).',
            'flowrate':
                'Rate of fluid movement.',
            'frequency':
                'The rate of cycling within a process. Typically used to describe voltage (and amperage) oscillation within AC power distribution components.',
            'humidity':
                'Concentration of water vapor in air (conditioned or unconditioned).',
            'illuminance':
                'Measurement of light.',
            'level':
                'The height of something with regard to a datum (e.g. the water level of a tank relative to the bottom).',
            'linearvelocity':
                'Example: wind speed',
            'percentage':
                'Measurement per hundred.',
            'powerfactor':
                'Ratio of real and apparent power.',
            'power':
                'Rate of energy consumption (assumed context is electrical and real, unless otherwise modified).',
            'pressure':
                'Measured force per unit area within a system or process.',
            'resistance':
                'Electrical resistance.',
            'specificenthalpy':
                'Measure of energy of air per unit mass.',
            'temperature':
                'Measures the temperature of media within a process or system.',
            'voltage':
                'Electrical potential difference between two reference points.',
            'volume':
                'The quantity of three-dimensional space contained by a closed surface.'
        },
        'measurement_descriptor': {
            'absolute':
                'Quality of media with respect to non-relativistic boudaries (e.g. absolute temperature).',
            'apparent':
                'The combination of reactive and real components (power).',
            'brightness':
                'Giving out or reflecting light; overall level of light in a space.',
            'charge':
                'The state of power storage (e.g. charged, not charged, discharged, etc.)',
            'closed':
                'Indicates full closed (for two-position actuators)',
            'deadband':
                'Represents a range in which the controller does not do anything.',
            'dewpoint':
                'The thermodynamic point at which water condenses from standing air.',
            'differential':
                'Measured difference between two reference points (e.g. differential_water_pressure)',
            'efficiency':
                'The ratio of required input to actual output. ',
            'end':
                'Indicates a final part of something, especially a period of time.',
            'extent':
                'Distance travelled.',
            'failed':
                'Indicates that a point is not operating as intended or is incapable of operating.',
            'lost':
                'Indicates that a point has lost some quality or quantity inadvertently.',
            'match':
                'A function that matches something against others.',
            'motion':
                'Detectable movement of a thing.',
            'index':
                "An integer which indicates the location of a particular data point in a list or numbered set (e.g. index 1 of ['a','b','c'] would return 'b', assuming the indexing starts at 0).",
            'offset':
                'The amount or distance by which something is out of line',
            'open':
                'Indicates full open (for two-position actuators).  This is the default sense if unspecified',
            'override':
                'An action that interrupts, cancels, or changes the current action or status.',
            'position':
                'A particular way in which something is placed or arranged, such as a door in the open position.',
            'reactive':
                'Power that is returned to the source (not consumed by the load).',
            'relative':
                'Quality of media with respect to theoretical minimum or maximum value for a given condition (e.g. relative humidity).',
            'run':
                'State of being active or operating. By default applies to control program for system (eg VAV program run_command).',
            'saturation':
                'Point at which no more of a material can be absorbed into another material.',
            'speed':
                'Numeric setting of how fast to run a device, in the specified untis. Typically used to describe revolutions of a motor as a fraction of nominal or maximum.',
            'start':
                'Indicates a point in time or space at which something has its origin or beginning.',
            'static':
                'Resting or stagnant value (e.g. static_pressure_sensor).',
            'thermal':
                'Relating to the transfer of heat.',
            'tilt':
                'Degree of radial rotation.',
            'wetbulb':
                'Describes air temperature measured at 100% relative humidity (saturation).'
        },
        'point_type': {
            'accumulator':
                'The total accumulated quantity (e.g. total energy accumulated).',
            'alarm':
                'A point that interprets some input values qualitatively (e.g. as good or bad, normal or in alarm, etc.). Alarms are always binary.',
            'capacity':
                'A design parameter quantity. Ex: design motor power capacity. Is always a maximum limit.',
            'counter':
                'Special case of accumulator that assumes integer values and non-dimensional units',
            'command':
                'The signal given to make an action happen. Defaults to multistate unless given a measurement type',
            'count':
                'Total count of actions or requests.',
            'label':
                'Identifying alias for component or system.',
            'mode':
                'Distinct mode of operation within system. Common example is economizer mode (enabled or disabled).',
            'requirement':
                'A lower limit design parameter (e.g. minimum flowrate requirement). Is always a lower limit.',
            'sensor':
                'Component used to measure some quality of a system or process. Can be feedback for an analog command.',
            'setpoint':
                'Control target of process or system.',
            'status':
                "The multistate value indicating an observed state in a piece of equipment, often indicating if a command was effected. It is a neutral observation (e.g. no quality judgment of 'good' or 'bad'). It also has no units of measurement (therefore if combined with a measurement subfield, it will indicate that the field is the directional status based on some measurement of that type, e.g. power_status equates to an on/off value based on some inference of power).",
            'specification':
                'The specified design value for a particular operating condition (differential pressure specification).',
            'timestamp':
                'An instant in time, represented as a numeric offset from the epoch.'
        }
    }])
