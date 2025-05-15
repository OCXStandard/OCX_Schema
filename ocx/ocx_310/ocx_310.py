from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDate, XmlDateTime


class LangValue(Enum):
    VALUE = ""


@dataclass
class BuilderInformationT:
    """
    Attributes:
        yard: Name of the construction yard.
        designer: The name of the designer of the vessel.
        owner: Contractor of the vessel.
        year_of_build: Keel laying date.
    """

    class Meta:
        name = "BuilderInformation_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    yard: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    designer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    year_of_build: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "yearOfBuild",
            "type": "Attribute",
        },
    )


@dataclass
class ClassNotationT:
    """
    Type definition of ClassNotation.

    Attributes:
        hull: The notation given to the hull of the ship by the
            classification society as a result of its approval
            activities done on the hull.
        machinery: The notation given to the machinery on the ship by
            the classification society as a result of its approval
            activities done on the machinery.
        ice_class: The type of class notation given to the ship
            indicating the ice conditions in which the ship has been
            approved to operate.
        service_area: The area or route in which the ship operates.
            NOTE: This may include information about waterway, wave,
            weather and wind conditions.                               .
        service_factor: The service area of the ship and the waves that
            occur in that area. The service factor should be in the
            range of 0.5 to 1.0.
        additional_notations: Additional notations assigned by the
            society.
    """

    class Meta:
        name = "ClassNotation_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    hull: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    machinery: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ice_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "iceClass",
            "type": "Attribute",
        },
    )
    service_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceArea",
            "type": "Attribute",
        },
    )
    service_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "serviceFactor",
            "type": "Attribute",
        },
    )
    additional_notations: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalNotations",
            "type": "Attribute",
        },
    )


@dataclass
class ClassParametersT:
    """
    Information that specifies design and intended performance characteristics of
    the ship in accordance with classification society rules and statutory
    regulations (see ISO                               10303-218, section 4.2.36).

    Attributes:
        block_coefficient_class: The ratio of the moulded displacement
            volume to the volume of a block that has its length equal to
            the length class, its breadth equal to the moulded breadth
            and its depth equal                                      to
            the scantlings draught (see ISO 10303-218, section
            4.2.32.1).
        design_speed_ahead: The forward speed at which the ship is
            designed to operate (see ISO 10303-218, section 4.2.32.2).
        design_speed_astern: The reverse speed at which the ship is
            designed to operate (see ISO 10303-218, section 4.2.32.3).
        length_solas: A length measurement for the ship measured in
            accordance with IMO IC110E (see ISO 10303-218, section
            4.2.32.5).
        length_class: A length measurement for the ship that is defined
            in classification society rules (see ISO 10303-218, section
            4.2.32.4).
        scantlings_draught: The summer load draught used by the
            classification society in its calculations for structural
            integrity and strength (see ISO 10303-218, section
            4.2.32.6).
    """

    class Meta:
        name = "ClassParameters_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    block_coefficient_class: Optional[float] = field(
        default=None,
        metadata={
            "name": "blockCoefficientClass",
            "type": "Attribute",
            "required": True,
        },
    )
    design_speed_ahead: Optional[float] = field(
        default=None,
        metadata={
            "name": "designSpeedAhead",
            "type": "Attribute",
        },
    )
    design_speed_astern: Optional[float] = field(
        default=None,
        metadata={
            "name": "designSpeedAstern",
            "type": "Attribute",
        },
    )
    length_solas: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthSolas",
            "type": "Attribute",
            "required": True,
        },
    )
    length_class: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthClass",
            "type": "Attribute",
            "required": True,
        },
    )
    scantlings_draught: Optional[float] = field(
        default=None,
        metadata={
            "name": "scantlingsDraught",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Description:
    """Contains a description of the component its parent represents.

    The description is stored as a string. You can use this element for
    whatever purposes you require. This element can be used inside many
    OCX XML elements but is optional.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class DescriptionT:
    class Meta:
        name = "Description_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HeaderT:
    """
    Type definition for the Header information for an XML instance.

    Attributes:
        time_stamp: Time stamp of the instance.
        name: Name of the XML instance.
        author: Name of author.
        originating_system: Name of originating system or application.
        organization: Name of originating organization.
        application_version: Version of originating application.
        documentation: Documentation of the content of the XML file.
    """

    class Meta:
        name = "Header_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    originating_system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    application_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class KnotVectorT:
    """
    Type definition of the NURBS knot vector.

    Attributes:
        value: The list of knots separated by  white space. Knots must
            be provided in increasing order.
    """

    class Meta:
        name = "KnotVector_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    value: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class Point3DT:
    """
    Type definition of a compact definition of  a point in 3D space composed of  a
    list of 3 X, Y and Z coordinate values all of same unit given by the unit ID.
    """

    class Meta:
        name = "Point3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    coordinates: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class QuantityT:
    """Type definition of the abstract base class for all types with values carrying a Unit : Q = v * u.

    Attributes:
        numericvalue: The numerical value of the quantity.
        unit: The reference to the unitsML reference unit.
    """

    class Meta:
        name = "Quantity_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    numericvalue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReferenceBaseT:
    """
    Type definition.

    Attributes:
        local_ref: References to an XML objects in the scope of the
            current file (internal references)
    """

    class Meta:
        name = "ReferenceBase_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    local_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "localRef",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReferencePlaneT:
    """
    Type definition of the concept of a reference plane which is typically used to
    define an unbounded geometry.
    """

    class Meta:
        name = "ReferencePlane_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ShipDesignationT:
    """The different types of identification given to the ship in order that it can
    be categorised by any shipping related organisation.

    It contains the minimal information which might
    be available about the ship.

    Attributes:
        ship_name: The name of the ship assigned by the owner.
        call_sign: The unique life-cycle identifier assigned to the ship
            by the flag state for radio communication.
        number_imo: A unique identification of a vessel according to IMO
            resolution A.600(15). It is made of the three letters “IMO”
            in front of the Lloyd’s Register number. This is a unique
            seven-digit number that is assigned to propelled, sea-going
            merchant ships of 100 GT and above upon keel laying (with
            some exceptions), see: IACS Procedural Requirements No. 11,
            IACS Procedure for Assigning Date of Build, 1996.
            https://www.imo.org/en/OurWork/IIIS/Pages/IMO-
            Identification-Number-Schemes.aspx: Information on IMO ship
            identification number scheme on the website of the IMO.
        ship_type: Optional string indicating the ship type.
    """

    class Meta:
        name = "ShipDesignation_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ship_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipName",
            "type": "Attribute",
            "required": True,
        },
    )
    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Attribute",
        },
    )
    number_imo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberIMO",
            "type": "Attribute",
        },
    )
    ship_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipType",
            "type": "Attribute",
        },
    )


@dataclass
class StatutoryDataT:
    """
    Type definition of vessel data related to the flag state.

    Attributes:
        port_registration: The national home port of the ship. The port
            of registration lies within the jurisdiction of the flag
            state (see ISO 10303-215, section 4.2.142.5).
        flag_state: The national authority with which the ship is
            registered (see ISO 10303-215, section 4.2.142.3).
    """

    class Meta:
        name = "StatutoryData_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    port_registration: Optional[str] = field(
        default=None,
        metadata={
            "name": "portRegistration",
            "type": "Attribute",
        },
    )
    flag_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "flagState",
            "type": "Attribute",
        },
    )


@dataclass
class Vector3DT:
    """
    Type definition of a unit vector.

    Attributes:
        direction: The unit vector components.
    """

    class Meta:
        name = "Vector3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    direction: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


class BulkCargoTypeValue(Enum):
    """
    Attributes:
        CEMENT: The bulk cargo is cement.
        COAL: The bulk cargo is coal.
        FISH: The bulk cargo is fish.
        GENERAL: The bulk cargo is of a general,non-specific type.
        GRAIN: The bulk cargo is grain.
        MUD: The bulk cargo is mud.
        ORE: The bulk cargo is ore.
        SUGAR: The bulk cargo is sugar.
        TIMBER: The bulk cargo is timber.
        UNSPECIFIED: The bulk cargo is of an unspecified type.
    """

    CEMENT = "cement"
    COAL = "coal"
    FISH = "fish"
    GENERAL = "general"
    GRAIN = "grain"
    MUD = "mud"
    ORE = "ore"
    SUGAR = "sugar"
    TIMBER = "timber"
    UNSPECIFIED = "unspecified"


class ClassificationSociety(Enum):
    """
    Enumeration of abbreviations for all Classification Societies.

    Attributes:
        ABS: American Bureau of Shipping.
        BK: Biro Klasifikasi Indonesia.
        BKR: Bulgarski Koraben Registar.
        BV: Bureau Veritas.
        CCS: China Classification Society.
        CR: China Register.
        CRS: Croatian Register of Shipping.
        CSC: Choson Classification Society.
        CSLPR: Cesky a Slovensky Lodni a Prumyslovy Registr.
        DNV: Det Norske Veritas.
        DSRK: Deutsche Schiffs-Revision und Klassifikation.
        FN: Fidenavis S.A.
        GL: Germanischer Lloyd.
        HR: Hellenic Register of Shipping.
        IRS: Indian Register of Shipping.
        KR: Korean Register of Shipping.
        LR: Lloyd’s Register.
        NK: Nippon Kaiji Kyokai.
        PRS: Polish Register of Shipping.
        RCB: Registro Cubano de Buques.
        RDS: Regjistri Detar Shqiptar.
        RINA: RINA Services S.p.A.
        RINAVE: Registro Internacional Naval, SA.
        RNR: Registrul Naval Roman.
        RR: Rechnoj Registr R.F.
        RRR: Russian River Register.
        RS: Russian Maritime Register of Shipping.
        TL: Turk Loydu Vakfi.
        UR: Shipping Register of Ukraine.
        VL: DNV GL.
        VR: Vietnam Register of Shipping.
    """

    ABS = "ABS"
    BK = "BK"
    BKR = "BKR"
    BV = "BV"
    CCS = "CCS"
    CR = "CR"
    CRS = "CRS"
    CSC = "CSC"
    CSLPR = "CSLPR"
    DNV = "DNV"
    DSRK = "DSRK"
    FN = "FN"
    GL = "GL"
    HR = "HR"
    IRS = "IRS"
    KR = "KR"
    LR = "LR"
    NK = "NK"
    PRS = "PRS"
    RCB = "RCB"
    RDS = "RDS"
    RINA = "RINA"
    RINAVE = "RINAVE"
    RNR = "RNR"
    RR = "RR"
    RRR = "RRR"
    RS = "RS"
    TL = "TL"
    UR = "UR"
    VL = "VL"
    VR = "VR"


class CompartmentPurposeValue(Enum):
    """
    Attributes:
        ACCESS_TRUNK: The compartment is designed to be used as an
            access trunk.&gt;
        AFT_PEAK_TANK: The compartment is a tank aft of the aftmost
            bulkhead of the ship.&gt;
        AUXILIARY_ENGINE_ROOM: The compartment is designed to be used as
            an auxiliary engine room space.&gt;
        BALLAST_TANK: The compartment is a watertight compartment to
            hold water ballast.&gt;
        BATTERY_ROOM: The compartment is designated for batteries.&gt;
        BERTHING_COMPARTMENT: The compartment is designed to be used as
            a berthing space.&gt;
        BOILER_ROOM: The compartment is designated for boilers.&gt;
        BOTTOM_WING_TANK: The compartment is a tank located between the
            ship side/bottom and a sloping longitudinal bulkhead. &gt;
        BOW_THRUSTER_ROOM: The compartment is designed to be used as the
            bow thruster room.&gt;
        CABIN: The compartment is designed to be used as a cabin
            space.&gt;
        CARGO_COMPARTMENT: The compartment is designed to carry liquid,
            bulk, or containerized goods. NOTE 1: These goods may be
            consumed during the voyage, as in the case of food or fuel,
            or they may be temporarily stored for transport between
            ports. NOTE 2: A tank compartment may also be used for the
            storage or transportation of liquid cargo. &gt;
        CENTRE_TANK: The compartment is a tank that occupies a large
            part of a ship cross section and that is symmetrical to the
            ship centre line.EXAMPLE: Crude oil tankers often have
            several centre tanks.&gt;
        CHAINLOCKER: The compartment is where anchor chain is
            stored.&gt;
        COFFERDAM: The compartment is a narrow void space between two
            bulkheads or floors that prevents leakage between the
            adjoining compartments.&gt;
        COMPRESSOR_ROOM: The compartment is designated for
            compressors.&gt;
        CONTROL: The compartment is designed to be used for ship command
            and control functions. &gt;
        CROSSOVER_TANK: The compartment is a tank used for dynamic
            stabilisation of the ship. &gt;
        DECK_TANK: The compartment is an independent tank located on the
            main deck.&gt;
        DEEP_TANK: The compartment is a tank extending from the bottom
            or inner bottom up to, or higher than, the lower deck. A
            deep tank is often fitted with hatches so that they may also
            be used for dry cargo in lieu of fuel oil, ballast water, or
            liquid cargo.&gt;
        DIVING_WELL: The compartment is a space for divers to exit to
            the sea through a hatch in the bottom of the vessel. &gt;
        DOUBLE_BOTTOM_AND_SIDE_TANK: The compartment is a tank located
            between the outer and inner bottom and bounded by an outer
            and inner side of the ship.&gt;
        DOUBLE_BOTTOM_TANK: The compartment is a tank located between
            the outer and inner bottom of the ship.&gt;
        DOUBLE_SIDE_TANK: The compartment is a tank between the outer
            ship side and the inner ship side.&gt;
        DRILL_WELL: The compartment is a space for drilling through an
            opening in the bottom of the vessel.&gt;
        DUCT_KEEL: The compartment is located between the bottom and the
            inner bottom running along the the centre line of the ship.
            &gt;
        ELECTRIC_MOTOR_ROOM: The compartment is designated for electric
            motors.&gt;
        EMERGENCY_FIRE_PUMP_ROOM: The compartment is designated for
            emergency fire pumps.&gt;
        EQUIPMENT_ROOM: The compartment is designated to be used as an
            equipment room. &gt;
        ESCAPE_TRUNK: The compartment is a vertical trunk fitted with a
            ladder to permit personnel to escape if trapped. Usually
            provided from the after end of the shaft tunnel to topside
            spaces.&gt;
        FORE_PEAK_TANK: The compartment is a tank located forward of the
            foremost bulkhead of the ship.&gt;
        FORECASTLE: The compartment is a superstructure fitted at the
            extreme forward end of the upper deck.&gt;
        HABITABLE_COMPARTMENT: The compartment is designed as a
            habitable space, which is primarily designated as suitable
            for occupancy by humans. Passenger safety and comfort are
            subject to international, national, class society, or other
            regulations usually covered by product specifications and
            applicable class and register notations.&gt;
        HEELING_TANK: The compartment is a tank used for adjusting the
            heeling of the ship.&gt;
        HOPPER_TANK: The compartment is a tank located between the ship
            side/bottom and a sloping longitudinal bulkhead. &gt;
        INSULATED_TANK: The compartment is a container constructed to
            hold one or more thermally insulated tanks for liquids &gt;
        LOUNGE: The compartment is designed to be used as a lounge
            space.&gt;
        MACHINERY_COMPARTMENT: The compartment is designed to contain
            machinery for the operation of the ship or in support of its
            mission. EXAMPLE: Engine room and bow thruster room are
            types of machinery compartments.&gt;
        MAIN_ENGINE_ROOM: The compartment is designed to be used as the
            main engine room.&gt;
        MEDICAL: The compartment is designed to be used as a medical
            space.&gt;
        PASSAGEWAY: The compartment is designed to be used as a
            passageway.&gt;
        POOP: The compartment is a superstructure fitted at the after
            end of the upper deck.&gt;
        PUMP_ROOM: The compartment is designated for pumps.&gt;
        RUDDER_TRUNK: The compartment is the trunk housing the rudder
            shaft.&gt;
        SEPARATOR_ROOM: The compartment is designated for
            separators.&gt;
        SETTLING_TANK: The compartment is a fuel oil tank used for
            separating entrained water from oil&gt;
        SHAFT_TUNNEL: The compartment is a watertight enclosure for the
            propeller shafting, large enough to walk in, extending aft
            from the engine room to provide access and protection to the
            shafting. Also known as a shaft alley.&gt;
        SIDE_TANK: The compartment is a tank located between the ship
            side and a longitudinal bulkhead.&gt;
        SIDE_WING_TANK: The compartment is a tank located between the
            ship side/bottom and a longitudinal bulkhead.&gt;
        STABILISER_ROOM: The compartment is designated for
            stabilisers.&gt;
        STABILITY_TANK: The compartment is a tank used for dynamic
            stabilisation of the ship.&gt;
        STEERING_GEAR_ROOM: The compartment is designated for steering
            gear.&gt;
        STERN_TANK: The compartment is a tank located at the aftmost
            location in the ship.&gt;
        STOOL_TANK: The compartment is a tank in the closed hull
            structure at either upper or lower end of a transverse
            bulkhead. &gt;
        TANK: The compartment is designed to carry liquids used in the
            mission of the ship, or for the storage of liquid cargoes
            transported by the ship. EXAMPLE: Fuels for propulsion of
            the ship, potable water for the passengers and crew, waste
            products, petroleum product cargo, and fuel for aircraft
            supported by the ship are carried in tank compartments.&gt;
        THRUSTER_ROOM: The compartment is designated for thrusters.&gt;
        TOP_WING_TANK: The compartment is a tank located between the
            ship side/deck and a sloping longitudinal bulkhead.&gt;
        TRIMMING_TANK: The compartment is a tank located near the ends
            of a ship. Seawater or fuel oil is carried in such tanks as
            necessary to change trim.&gt;
        TRUNK: The compartment is a vertical or inclined space or
            passage formed by bulkheads or casings, extending one or
            more deck heights, around openings in the decks, through
            which access can be obtained and cargo or stores handled, or
            ventilation provided without disturbing or interfering with
            the contents or arrangements of the adjoining spaces.&gt;
        USER_DEFINED: The compartment function is other than one of the
            pre-defined values and is specified by the user_def_function
            attribute.&gt;
        VOID: The compartment is designed as an inaccessible, closed
            space that is never used to carry cargo or to be regularly
            occupied by humans. The main uses of a void compartment are
            segregating the cargo and fluids that are necessary to
            operate the ship, or to provide emergency access to other
            spaces.&gt;
        WATERJET_ROOM: The compartment is designated for waterjets.&gt;
        WHEELHOUSE: The compartment is designated for primary steerage
            and control of the ship. Also known as the bridge.&gt;
        WING_TANK: The compartment is a tank located well outboard
            adjacent to the side shell plating, often consisting of a
            continuation of the double bottom up the sides to a deck or
            flat.&gt;
    """

    ACCESS_TRUNK = "access_trunk"
    AFT_PEAK_TANK = "aft_peak_tank"
    AUXILIARY_ENGINE_ROOM = "auxiliary_engine_room"
    BALLAST_TANK = "ballast_tank"
    BATTERY_ROOM = "battery_room"
    BERTHING_COMPARTMENT = "berthing_compartment"
    BOILER_ROOM = "boiler_room"
    BOTTOM_WING_TANK = "bottom_wing_tank"
    BOW_THRUSTER_ROOM = "bow_thruster_room"
    CABIN = "cabin"
    CARGO_COMPARTMENT = "cargo_compartment"
    CENTRE_TANK = "centre_tank"
    CHAINLOCKER = "chainlocker"
    COFFERDAM = "cofferdam"
    COMPRESSOR_ROOM = "compressor_room"
    CONTROL = "control"
    CROSSOVER_TANK = "crossover_tank"
    DECK_TANK = "deck_tank"
    DEEP_TANK = "deep_tank"
    DIVING_WELL = "diving_well"
    DOUBLE_BOTTOM_AND_SIDE_TANK = "double_bottom_and_side_tank"
    DOUBLE_BOTTOM_TANK = "double_bottom_tank"
    DOUBLE_SIDE_TANK = "double_side_tank"
    DRILL_WELL = "drill_well"
    DUCT_KEEL = "duct_keel"
    ELECTRIC_MOTOR_ROOM = "electric_motor_room"
    EMERGENCY_FIRE_PUMP_ROOM = "emergency_fire_pump_room"
    EQUIPMENT_ROOM = "equipment_room"
    ESCAPE_TRUNK = "escape_trunk"
    FORE_PEAK_TANK = "fore_peak_tank"
    FORECASTLE = "forecastle"
    HABITABLE_COMPARTMENT = "habitable_compartment"
    HEELING_TANK = "heeling_tank"
    HOPPER_TANK = "hopper_tank"
    INSULATED_TANK = "insulated_tank"
    LOUNGE = "lounge"
    MACHINERY_COMPARTMENT = "machinery_compartment"
    MAIN_ENGINE_ROOM = "main_engine_room"
    MEDICAL = "medical"
    PASSAGEWAY = "passageway"
    POOP = "poop"
    PUMP_ROOM = "pump_room"
    RUDDER_TRUNK = "rudder_trunk"
    SEPARATOR_ROOM = "separator_room"
    SETTLING_TANK = "settling_tank"
    SHAFT_TUNNEL = "shaft_tunnel"
    SIDE_TANK = "side_tank"
    SIDE_WING_TANK = "side_wing_tank"
    STABILISER_ROOM = "stabiliser_room"
    STABILITY_TANK = "stability_tank"
    STEERING_GEAR_ROOM = "steering_gear_room"
    STERN_TANK = "stern_tank"
    STOOL_TANK = "stool_tank"
    TANK = "tank"
    THRUSTER_ROOM = "thruster_room"
    TOP_WING_TANK = "top_wing_tank"
    TRIMMING_TANK = "trimming_tank"
    TRUNK = "trunk"
    USER_DEFINED = "user_defined"
    VOID = "void"
    WATERJET_ROOM = "waterjet_room"
    WHEELHOUSE = "wheelhouse"
    WING_TANK = "wing_tank"


class CurveFormEnum(Enum):
    """
    Enumerator of NURBS curve forms.

    Attributes:
        UNKNOWN: An unknown curve form.
        OPEN: An open curve form.
        CLOSED: A closed curve form with C0 continuity.
        PERIODIC: A closed curve form wit C1 continuity.
    """

    UNKNOWN = "Unknown"
    OPEN = "Open"
    CLOSED = "Closed"
    PERIODIC = "Periodic"


class FreeboardTypeValue(Enum):
    """
    Attributes:
        A: A type A ship is one which is designed to carry only liquid
            cargoes in bulk, and in which cargo tanks have only small
            access openings closed by watertight gasketed covers of
            steel or equivalent material.
        B: All ships which do not come within the provisions regarding
            Type A ships shall be considered as Type B ships.
            .
    """

    A = "A"
    B = "B"


class FunctionTypeValue(Enum):
    """
    Attributes:
        BRACKET: A supporting plate.
        BRACKET_END_BRACKET: A bracket attached to the end of stiffener.
        BRACKET_TRIPPING: A bracket used to support a load bearing
            element in between primary supporting members.
        CASING: Casing is the covering or bulkhead around or about any
            space for protection.
        CASING_ENGINE_ROOM: Casing is the covering or bulkhead
            protection.
        DECK: Deck Structure is the deck plating with stiffeners,
            girders and supporting pillars.
        DECK_ACCOMMODATION_DECK: Deck Structure is the deck plating with
            stiffeners, girders and supporting pillars.
        DECK_CARGO_DECK: Deck Structure is the deck plating with
            stiffeners, girders and supporting pillars.
        DECK_CROSS_DECK: Cross Deck is the area between cargo hatches.
        DECK_CROSS_TIES: Cross Ties are used to support the longitudinal
            bulkheads of oil tankers against hydrostatic and
            hydrodynamic loads.
        DECK_FLOOR: Floor is a bottom transverse member.
        DECK_WEATHER_DECK: Weather deck is normally the uppermost
            complete deck exposed to weather and sea, which has
            permanent means of closing all exposed openings.
        DECK_FORECASTLE_DECK: Forecastle deck is a deck attached to the
            short superstructure situated at the bow.
        DECK_FREEBOARD_DECK: Free board deck is the first deck above the
            waterline.
        DECK_GIRDER: Deck Structure is the deck plating with primary
            girder members.
        DECK_INNER_BOTTOM_DECK: Deck Structure is the deck plating with
            stiffeners, girders and supporting pillars.
        DECK_PLATFORM_DECK: Deck Structure is the deck plating with
            stiffeners, girders and supporting pillars.
        DECK_POOP_DECK: Poop Deck is the first deck above the shelter
            deck at aft end of a ship.
        DECK_STRENGTH_DECK: Strength Deck is normally the uppermost
            continuous deck. After special consideration of its
            effectiveness, another deck may be defined as strength deck.
        DECK_SUPERSTRUCTURE_DECK: Superstructure is a decked structure
            on the free-board deck extending for at least 92% of the
            breadth of the ship.
        DECK_TRUNK_DECK: Deck Structure is the deck plating with
            stiffeners, girders and supporting pillars.
        DECK_TWEEN_DECK: Tween Decks is an abbreviation of between
            decks, placed between the upper deck and the tank top in the
            cargo holds.
        DECK_WHEELHOUSE_DECK: Deck House is a structure on the free-
            board or superstructure deck not extending from side to side
            of the ship.
        FOUNDATION: Supporting foundation structure .
        FOUNDATION_ENGINE: Engine foundation including foundation top
            plate .
        HATCHWAY_COAMING: Hatch Coming is the vertical plating built
            around the hatchways to prevent water from entering the
            hold; and to serve as a framework for the hatch covers.
        HATCHWAY_COAMING_END_COAMING: Hatch Coming is the vertical
            plating built around the hatchways to prevent water from
            entering the hold; and to serve as a framework for the hatch
            covers.
        HATCHWAY_COAMING_SIDE_COAMING: Hatch Coming is the vertical
            plating built around the hatchways to prevent water from
            entering the hold; and to serve as a framework for the hatch
            covers.
        HATCH_COVER: Hatch Covers are wooden or steel covers fitted over
            a hatchway to prevent the ingress of water into the ship s
            hold and may also be the supporting structure for deck
            cargo.
        HATCH_COVER_HATCH_TOP: Hatch Covers are wooden or steel covers
            fitted over a hatchway to prevent the ingress of water into
            the ship s hold and may also be the supporting structure for
            deck cargo.
        LONGITUDINAL: Longitudinal stiffening system.
        LONGITUDINAL_BULKHEAD: Bulkhead Structure longitudinal bulkhead
            plating with stiffeners and girders.
        LONGITUDINAL_CENTERLINE_BULKHEAD: Bulkhead Structure
            longitudinal bulkhead plating with stiffeners and girders.
        LONGITUDINAL_GIRDER: Girder is a collective term for primary
            supporting structural members.
        LONGITUDINAL_CENTERLINE_GIRDER: Girder is a collective term for
            primary supporting structural members.
        LONGITUDINAL_CENTERLINE_SIDE_GIRDER: Girder is a collective term
            for primary supporting structural members.
        LONGITUDINAL_DOUBLE_BOTTOM: Double Bottom Structure is the shell
            plating with stiffeners below the top of the inner bottom
            and other elements below and including the inner bottom
            plating.
        LONGITUDINAL_TOP_TANK: A top tank used for ballast or for
            stability typically used in container vessels.
        LONGITUDINAL_HOPPER_SIDE_LOWER: Hopper Side Tanks are tanks used
            for ballast or for stability when carrying certain cargoes
            in bulk carriers. Also referred to as upper wing ballast
            tanks.
        LONGITUDINAL_HOPPER_SIDE_UPPER: Hopper Side Tanks are tanks used
            for ballast or for stability when carrying certain cargoes
            in bulk carriers. Also referred to as lower wing ballast
            tanks.     .
        LONGITUDINAL_INNER_BOTTOM: Longitudinal stiffening system in
            inner bottom.
        LONGITUDINAL_LOWER_STOOL_BOTTOM_PLATE: Stool is a structure
            supporting cargo hold and tank bulkheads.
        LONGITUDINAL_LOWER_STOOL_TOP_PLATE: Stool is a structure
            supporting cargo hold and tank bulkheads.
        LONGITUDINAL_LOWER_STOOL: Stool is a structure supporting cargo
            hold and tank bulkheads.
        LONGITUDINAL_SIDE_GIRDER: Longitudinal stiffening system.
        LONGITUDINAL_STRINGER: Longitudinal (flat) stiffening system.
        LONGITUDINAL_SIDE_STRINGER: Longitudinal (flat) stiffening
            system at side.
        LONGITUDINAL_SKEG: Narrow vertical part added to the hull in the
            stern.
        LONGITUDINAL_UPPER_STOOL: Supporting structure for transverse
            bulkhead.
        LONGITUDINAL_WASH_BULKHEAD: Wash Bulkhead is a perforated or
            partial bulkhead in a tank.
        PLATING_LUG: A lug or collar plate used to support a stiffener
            penetrating a primary supporting member.
        PLATING_GUSSET: Gusset is a triangular plate, usually fitted to
            distribute forces at a strength connection between two
            structural members.
        PLATING_SHEDDER: Shedder Plates are slanted plates fitted in dry
            cargo holds to prevent undesired pockets of cargo. The term
            is also commonly applied to slanted plates that are fitted
            to improve the structural stability of corrugated bulkheads
            and framing members..
        SHEER_STRAKE: Sheer strake is the top strake of a ships side
            shell plating.
        SHELL: The watertight shell plating of the hull.
        SHELL_BILGE_KEEL: Bilge Keel is a piece of plate set
            perpendicular to a ship’s shell along her bilges for about
            one third her length to reduce rolling..
        SHELL_BILGE_STRAKE: Bilge strake is the strake at the turn of
            bilge extending outward to a point where the side rises
            vertically.
        SHELL_BOTTOM_SHELL: The watertight shell plating of the bottom
            of the hull.
        SHELL_BULWARK_SHELL: Bulwark is the vertical plating immediately
            above the upper edge of the ship’s side surrounding the
            exposed deck(s).
        SHELL_INNER_BOTTOM_SHELL: The watertight shell plating of the
            hull inner bottom.
        SHELL_INNER_SIDE_SHELL: The watertight shell plating located at
            the inners side of the hull.
        SHELL_SUPERSTRUCTURE_SIDE: The watertight shell plating at the
            superstructure side.
        SUPERSTRUCTURE: Superstructure is a decked structure on the
            free-board deck extending for at least 92% of the breadth of
            the ship. Often named deck-house or wheelhouse.
        SUPERSTRUCTURE_DECKHOUSE_AFT: Superstructure/Wheelhouse aft.
        SUPERSTRUCTURE_DECKHOUSE_FRONT: Superstructure/Wheelhouse front.
        SUPERSTRUCTURE_DECKHOUSE_SIDE: Superstructure/Wheelhouse side.
        SUPERSTRUCTURE_DECKHOUSE_TOP: Superstructure/Wheelhouse top.
        SUPERSTRUCTURE_SIDE: Superstructure/Wheelhouse side.
        TRANSVERSAL: Transverse stiffening system.
        TRANSVERSAL_BULKHEAD: Bulkhead transverse stiffening system.
        TRANSVERSAL_BULKHEAD_ACCOMMODATION: Bulkhead transverse
            stiffening system in the accommodation area.
        TRANSVERSAL_BULKHEAD_AFT_PEAK: Bulkhead transverse stiffening
            system at aft peak.
        TRANSVERSAL_BULKHEAD_COLLISION: Transverse stiffening system in
            the collision bulkhead.
        TRANSVERSAL_BULKHEAD_CORRUGATED: Transverse stiffening system in
            the form of plate corrugations.
        TRANSVERSAL_BULKHEAD_LOWER_STOOL: The lower stool supporting
            structure of the transverse cargo hold and tank bulkheads.
        TRANSVERSAL_BULKHEAD_PARTIAL: A partial transverse bulkhead
            stiffening system.
        TRANSVERSAL_BULKHEAD_UPPER_STOOL: The upper stool supporting
            structure of the transverse cargo hold and tank bulkheads.
        TRANSVERSAL_BULKHEAD_WASH: Wash Bulkhead is a perforated or
            partial bulkhead in a tank.
        UNDEFINED_MISCELLANEOUS: Undefined structure function.
        VERTICAL: A vertical stiffening system.
        WEB_FRAME: A transverse stiffening system.
        WEB_FRAME_BILGE: A transverse stiffening system in the bilge
            area.
        WEB_FRAME_DECK_TRANSVERSE_FRAME: A transverse stiffening system
            of a deck.
        WEB_FRAME_FLOOR_FRAME: A transverse stiffening system of a
            floor.
        WEB_FRAME_GENERAL_WEB_FRAME: A transverse stiffening system.
        WEB_FRAME_HORIZONTAL: A transverse stiffening system.
        WEB_FRAME_VERTICAL: A transverse stiffening system part of a
            vertical structure.
        WEB_FRAME_MAIN_FRAME: A transverse stiffening system
            representing the main frame of the vessel.
        WEB_FRAME_TOPSIDE_TANK: A transverse stiffening system.
        WEB_FRAME_SIDE: A transverse stiffening system.
        WEB_FRAME_TWEEN_DECK_FRAME: Tween Decks is an abbreviation of
            between decks, placed between the upper deck and the tank
            top in the cargo holds.
    """

    BRACKET = "BRACKET"
    BRACKET_END_BRACKET = "BRACKET: End bracket"
    BRACKET_TRIPPING = "BRACKET: Tripping"
    CASING = "CASING"
    CASING_ENGINE_ROOM = "CASING: Engine room"
    DECK = "DECK"
    DECK_ACCOMMODATION_DECK = "DECK: Accommodation deck"
    DECK_CARGO_DECK = "DECK: Cargo deck"
    DECK_CROSS_DECK = "DECK: Cross deck"
    DECK_CROSS_TIES = "DECK: Cross ties"
    DECK_FLOOR = "DECK: Floor"
    DECK_WEATHER_DECK = "DECK: Weather deck"
    DECK_FORECASTLE_DECK = "DECK: Forecastle deck"
    DECK_FREEBOARD_DECK = "DECK: Freeboard deck"
    DECK_GIRDER = "DECK: Girder"
    DECK_INNER_BOTTOM_DECK = "DECK: Inner bottom deck"
    DECK_PLATFORM_DECK = "DECK: Platform deck"
    DECK_POOP_DECK = "DECK: Poop deck"
    DECK_STRENGTH_DECK = "DECK: Strength deck"
    DECK_SUPERSTRUCTURE_DECK = "DECK: Superstructure deck"
    DECK_TRUNK_DECK = "DECK: Trunk deck"
    DECK_TWEEN_DECK = "DECK: Tween deck"
    DECK_WHEELHOUSE_DECK = "DECK: Wheelhouse deck"
    FOUNDATION = "FOUNDATION"
    FOUNDATION_ENGINE = "FOUNDATION: Engine"
    HATCHWAY_COAMING = "HATCHWAY_COAMING"
    HATCHWAY_COAMING_END_COAMING = "HATCHWAY_COAMING: End coaming"
    HATCHWAY_COAMING_SIDE_COAMING = "HATCHWAY_COAMING: Side coaming"
    HATCH_COVER = "HATCH_COVER"
    HATCH_COVER_HATCH_TOP = "HATCH_COVER: Hatch top"
    LONGITUDINAL = "LONGITUDINAL"
    LONGITUDINAL_BULKHEAD = "LONGITUDINAL: Bulkhead"
    LONGITUDINAL_CENTERLINE_BULKHEAD = "LONGITUDINAL: Centerline bulkhead"
    LONGITUDINAL_GIRDER = "LONGITUDINAL: Girder"
    LONGITUDINAL_CENTERLINE_GIRDER = "LONGITUDINAL: Centerline girder"
    LONGITUDINAL_CENTERLINE_SIDE_GIRDER = (
        "LONGITUDINAL: Centerline side girder"
    )
    LONGITUDINAL_DOUBLE_BOTTOM = "LONGITUDINAL: Double bottom"
    LONGITUDINAL_TOP_TANK = "LONGITUDINAL: Top tank"
    LONGITUDINAL_HOPPER_SIDE_LOWER = "LONGITUDINAL: Hopper side lower"
    LONGITUDINAL_HOPPER_SIDE_UPPER = "LONGITUDINAL: Hopper side upper"
    LONGITUDINAL_INNER_BOTTOM = "LONGITUDINAL: Inner bottom"
    LONGITUDINAL_LOWER_STOOL_BOTTOM_PLATE = (
        "LONGITUDINAL: Lower stool bottom plate"
    )
    LONGITUDINAL_LOWER_STOOL_TOP_PLATE = "LONGITUDINAL: Lower stool top plate"
    LONGITUDINAL_LOWER_STOOL = "LONGITUDINAL: Lower stool"
    LONGITUDINAL_SIDE_GIRDER = "LONGITUDINAL: Side girder"
    LONGITUDINAL_STRINGER = "LONGITUDINAL: Stringer"
    LONGITUDINAL_SIDE_STRINGER = "LONGITUDINAL: Side stringer"
    LONGITUDINAL_SKEG = "LONGITUDINAL: Skeg"
    LONGITUDINAL_UPPER_STOOL = "LONGITUDINAL: Upper stool"
    LONGITUDINAL_WASH_BULKHEAD = "LONGITUDINAL: Wash bulkhead"
    PLATING_LUG = "PLATING: Lug"
    PLATING_GUSSET = "PLATING: Gusset"
    PLATING_SHEDDER = "PLATING: Shedder"
    SHEER_STRAKE = "SHEER_STRAKE"
    SHELL = "SHELL"
    SHELL_BILGE_KEEL = "SHELL: Bilge keel"
    SHELL_BILGE_STRAKE = "SHELL: Bilge strake"
    SHELL_BOTTOM_SHELL = "SHELL: Bottom shell"
    SHELL_BULWARK_SHELL = "SHELL: Bulwark shell"
    SHELL_INNER_BOTTOM_SHELL = "SHELL: Inner bottom shell"
    SHELL_INNER_SIDE_SHELL = "SHELL: Inner side shell"
    SHELL_SUPERSTRUCTURE_SIDE = "SHELL: Superstructure side"
    SUPERSTRUCTURE = "SUPERSTRUCTURE"
    SUPERSTRUCTURE_DECKHOUSE_AFT = "SUPERSTRUCTURE: Deckhouse aft"
    SUPERSTRUCTURE_DECKHOUSE_FRONT = "SUPERSTRUCTURE: Deckhouse front"
    SUPERSTRUCTURE_DECKHOUSE_SIDE = "SUPERSTRUCTURE: Deckhouse side"
    SUPERSTRUCTURE_DECKHOUSE_TOP = "SUPERSTRUCTURE: Deckhouse top"
    SUPERSTRUCTURE_SIDE = "SUPERSTRUCTURE: Side"
    TRANSVERSAL = "TRANSVERSAL"
    TRANSVERSAL_BULKHEAD = "TRANSVERSAL_BULKHEAD"
    TRANSVERSAL_BULKHEAD_ACCOMMODATION = "TRANSVERSAL_BULKHEAD: Accommodation"
    TRANSVERSAL_BULKHEAD_AFT_PEAK = "TRANSVERSAL_BULKHEAD: Aft peak"
    TRANSVERSAL_BULKHEAD_COLLISION = "TRANSVERSAL_BULKHEAD: Collision"
    TRANSVERSAL_BULKHEAD_CORRUGATED = "TRANSVERSAL_BULKHEAD: Corrugated"
    TRANSVERSAL_BULKHEAD_LOWER_STOOL = "TRANSVERSAL_BULKHEAD: Lower stool"
    TRANSVERSAL_BULKHEAD_PARTIAL = "TRANSVERSAL_BULKHEAD: Partial"
    TRANSVERSAL_BULKHEAD_UPPER_STOOL = "TRANSVERSAL_BULKHEAD: Upper stool"
    TRANSVERSAL_BULKHEAD_WASH = "TRANSVERSAL_BULKHEAD: Wash"
    UNDEFINED_MISCELLANEOUS = "UNDEFINED: Miscellaneous"
    VERTICAL = "VERTICAL"
    WEB_FRAME = "WEB_FRAME"
    WEB_FRAME_BILGE = "WEB_FRAME: Bilge"
    WEB_FRAME_DECK_TRANSVERSE_FRAME = "WEB_FRAME: Deck transverse frame"
    WEB_FRAME_FLOOR_FRAME = "WEB_FRAME: Floor frame"
    WEB_FRAME_GENERAL_WEB_FRAME = "WEB_FRAME: General web-frame"
    WEB_FRAME_HORIZONTAL = "WEB_FRAME: Horizontal"
    WEB_FRAME_VERTICAL = "WEB_FRAME: Vertical"
    WEB_FRAME_MAIN_FRAME = "WEB_FRAME: Main frame"
    WEB_FRAME_TOPSIDE_TANK = "WEB_FRAME: Topside tank"
    WEB_FRAME_SIDE = "WEB_FRAME: Side"
    WEB_FRAME_TWEEN_DECK_FRAME = "WEB_FRAME: Tween deck frame"


class GeometryFormatValue(Enum):
    """
    Attributes:
        IGS: IGES file representing one the detailed geometry of a
            structural part (Bracket, Stiffener, Pillar, Plate).
        JT: OpenJT file representing one the detailed geometry of a
            structural part (Bracket, Stiffener, Pillar, Plate).
        STP: STEP file representing one the detailed geometry of a
            structural part (Bracket, Stiffener, Pillar, Plate). This is
            the default format.
    """

    IGS = ".igs"
    JT = ".jt"
    STP = ".stp"


class GradeValue(Enum):
    """
    Attributes:
        A: Normal strength steel. Ref. IACS UR W11.
        B: Normal strength steel. Ref. IACS UR W11.
        C: Normal strength steel. Ref. IACS UR W11.
        D: Normal strength steel. Ref. IACS UR W11.
        A32: High strength steel. Ref. IACS UR W11.
        D32: High strength steel. Ref. IACS UR W11.
        E32: High strength steel. Ref. IACS UR W11.
        F32: High strength steel. Ref. IACS UR W11.
        A36: High strength steel. Ref. IACS UR W11.
        D36: High strength steel. Ref. IACS UR W11.
        E36: High strength steel. Ref. IACS UR W11.
        F36: High strength steel. Ref. IACS UR W11.
        A40: High strength steel. Ref. IACS UR W11.
        D40: High strength steel. Ref. IACS UR W11.
        E40: High strength steel. Ref. IACS UR W11.
        F40: High strength steel. Ref. IACS UR W11.
    """

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    A32 = "A32"
    D32 = "D32"
    E32 = "E32"
    F32 = "F32"
    A36 = "A36"
    D36 = "D36"
    E36 = "E36"
    F36 = "F36"
    A40 = "A40"
    D40 = "D40"
    E40 = "E40"
    F40 = "F40"


class LiquidCargoTypeValue(Enum):
    """
    Attributes:
        ALCOHOL: The cargo is alcohol.
        AMMONIA: The cargo is ammonia.
        ASPHALT: The cargo is asphalt.
        AVIATION_OIL: The cargo is aviation oil.
        CAUSTIC_SODA: The cargo is caustic soda.
        CEMENT: The cargo is liquid cement.
        CHEMICAL: The cargo is a liquid chemical.
        CRUDE_OIL: The cargo is crude oil.
        EDIBLE_OIL: The cargo is edible oil.
        FUEL_OIL: The cargo is fuel oil.
        FRESH_WATER: The cargo is fresh water.
        HYDROCHLORIDE_ACID: The cargo is hydrochloride acid.
        LUBRICATING_OIL: The cargo is lubrication oil.
        METHANOL: The cargo is methanol.
        MOLASSES: The cargo is molasses.
        PRODUCT_OIL: The cargo is product oil.
        SALT_WATER: The cargo is salt water.
        SULLAGE: The cargo is sullage.
        SLUDGE: The cargo is sludge.
        SULPHUR: The cargo is sulphur.
        VEGETABLE_OIL: The cargo is vegetable oil.
        WATER_BALLAST: The cargo is water ballast.
        WINE: The cargo is wine.
        UNSPECIFIED: The cargo is of an unspecified type.
    """

    ALCOHOL = "alcohol"
    AMMONIA = "ammonia"
    ASPHALT = "asphalt"
    AVIATION_OIL = "aviation oil"
    CAUSTIC_SODA = "caustic soda"
    CEMENT = "cement"
    CHEMICAL = "chemical"
    CRUDE_OIL = "crude oil"
    EDIBLE_OIL = "edible oil"
    FUEL_OIL = "fuel oil"
    FRESH_WATER = "fresh water"
    HYDROCHLORIDE_ACID = "hydrochloride acid"
    LUBRICATING_OIL = "lubricating oil"
    METHANOL = "methanol"
    MOLASSES = "molasses"
    PRODUCT_OIL = "product oil"
    SALT_WATER = "salt water"
    SULLAGE = "sullage"
    SLUDGE = "sludge"
    SULPHUR = "sulphur"
    VEGETABLE_OIL = "vegetable oil"
    WATER_BALLAST = "water ballast"
    WINE = "wine"
    UNSPECIFIED = "unspecified"


class ManufactureValue(Enum):
    ROLLED = "Rolled"
    WELDED = "Welded"


class PositionValue(Enum):
    """
    Attributes:
        NEAR_SIDE: The bracket is at the near side of a penetration.
        FAR_SIDE: The bracket is at the far side of a penetration.
    """

    NEAR_SIDE = "Near side"
    FAR_SIDE = "Far side"


class RefTypeValue(Enum):
    """
    Allowable OCX types which can be referenced using the ocxItemPtr.

    Attributes:
        OCX_PANEL: A reference to an instantiated  structure composition
            of type Panel.
        OCX_PLATE: A reference to an instantiated structure part of type
            Plate.
        OCX_SEAM: A reference to an instantiated structure composition
            of type Seam.
        OCX_BRACKET: A reference to an instantiated structure part of
            type Bracket.
        OCX_STIFFENER: A reference to an instantiated structure part of
            type Stiffener.
        OCX_PILLAR: A reference to an instantiated structure part of
            type Pillar.
        OCX_CONNECTION_CONFIGURATION: A reference to an instantiated
            stiffener configuration.
        OCX_HOLE2_D: A reference to a catalogue 2D hole shape.
        OCX_MATERIAL: A reference to a catalogue material.
        OCX_BAR_SECTION: A reference to a catalogue bar section.
        OCX_CELL: A reference to an instantiated compartment cell.
        OCX_VESSEL: A reference to the vessel instance.
        OCX_FREE_EDGE_CURVE3_D: A reference to an instantiated free edge
            geometry.
        OCX_SURFACE: A reference to an instantiated surface.
        OCX_END_CUT: A reference to a stiffener end cut.
        OCX_OCCURRENCE_GROUP: A reference to an occurrence group in a
            design view.
        OCX_EDGE_REINFORCEMENT: A reference to an an edge reinforcement.
        OCX_HOLE2_DCONTOUR: A reference to a hole/cut-out contour.
        OCX_REFERENCE_PLANE:
    """

    OCX_PANEL = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Panel"
    )
    OCX_PLATE = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Plate"
    )
    OCX_SEAM = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Seam"
    )
    OCX_BRACKET = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Bracket"
    )
    OCX_STIFFENER = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Stiffener"
    )
    OCX_PILLAR = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Pillar"
    )
    OCX_CONNECTION_CONFIGURATION = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}ConnectionConfiguration"
    )
    OCX_HOLE2_D = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Hole2D"
    )
    OCX_MATERIAL = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Material"
    )
    OCX_BAR_SECTION = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}BarSection"
    )
    OCX_CELL = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Cell"
    )
    OCX_VESSEL = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Vessel"
    )
    OCX_FREE_EDGE_CURVE3_D = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}FreeEdgeCurve3D"
    )
    OCX_SURFACE = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Surface"
    )
    OCX_END_CUT = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}EndCut"
    )
    OCX_OCCURRENCE_GROUP = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}OccurrenceGroup"
    )
    OCX_EDGE_REINFORCEMENT = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}EdgeReinforcement"
    )
    OCX_HOLE2_DCONTOUR = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}Hole2DContour"
    )
    OCX_REFERENCE_PLANE = QName(
        "{https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd}ReferencePlane"
    )


class ReinforcementTypeValue(Enum):
    """
    Attributes:
        FLANGED: The bracket edge has a flanged stiffening with a bend
            radius.
        FACE_PLATE: The bracket edge has a faceplate.
        BUCKLING_STIFFENER: The bracket edge has a buckling stiffener.
    """

    FLANGED = "Flanged"
    FACE_PLATE = "FacePlate"
    BUCKLING_STIFFENER = "BucklingStiffener"


class SlotTypeValue(Enum):
    SLIT = "Slit"
    OPEN = "Open"


class TightnessValue(Enum):
    """
    Attributes:
        NON_TIGHT: The panel or plate in not water tight.
        WATER_TIGHT: The panel or plate in water tight.
        GAS_TIGHT: The panel or plate in gas tight, but not water tight.
        UNDEFINED: The panel or plate has no tightness defined.
    """

    NON_TIGHT = "NonTight"
    WATER_TIGHT = "WaterTight"
    GAS_TIGHT = "GasTight"
    UNDEFINED = "Undefined"


class UnitCargoTypeValue(Enum):
    """
    Attributes:
        AIRCRAFT: The unit cargo is aircraft.
        BOAT: The unit cargo is boat.
        CABLE: The unit cargo is cable.
        CONTAINER: The unit cargo is container.
        DRUMS: The unit cargo is drums.
        LIVESTOCK: The unit cargo is livestock.
        PALLET: The unit cargo is pallet.
        TRAILER: The unit cargo is trailer.
        VEHICLE: The unit cargo is vehicle.
        UNSPECIFIED: The unit cargo is of unspecified type.
    """

    AIRCRAFT = "aircraft"
    BOAT = "boat"
    CABLE = "cable"
    CONTAINER = "container"
    DRUMS = "drums"
    LIVESTOCK = "livestock"
    PALLET = "pallet"
    TRAILER = "trailer"
    VEHICLE = "vehicle"
    UNSPECIFIED = "unspecified"


@dataclass
class AmountOfSubstanceType:
    """
    Type of the quantity amount of substance.

    Attributes:
        symbol: Symbol of the quantity amount of substance.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="N",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class ElectricCurrentType:
    """
    Type of the quantity electric current.

    Attributes:
        symbol: Symbol of the quantity electric current.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="I",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


class EnumeratedRootUnitTypePrefix(Enum):
    """
    Attributes:
        Y: yotta: septillion
        Z: zetta: sextillion
        E: exa: quintillion
        P: peta: quadrillion
        T: tera: trillion
        G: giga: billion
        M: mega: million
        K: kilo: thousand
        H: hecto: hundred
        DA: deka: ten
        D: deci: tenth
        C: centi: hundredth
        M_1: milli: thousandth
        MU: micro: millonth
        N: nano: billonth
        P_1: pico: trillionth
        F: femto: quadrillionth
        A: atto: quintillionth
        Z_1: zepto: sextillionth:
        Y_1: yocto: septillionth
        KI: kibi: kilobinary
        MI: mebi: magabinary
        GI: gibi: gigabinary
        TI: tebi: terabinary
        ZI: pebi: petabinary
        EI: exbi: exabinary
        YI: yobi: yottabinary
    """

    Y = "Y"
    Z = "Z"
    E = "E"
    P = "P"
    T = "T"
    G = "G"
    M = "M"
    K = "k"
    H = "h"
    DA = "da"
    D = "d"
    C = "c"
    M_1 = "m"
    MU = "mu"
    N = "n"
    P_1 = "p"
    F = "f"
    A = "a"
    Z_1 = "z"
    Y_1 = "y"
    KI = "Ki"
    MI = "Mi"
    GI = "Gi"
    TI = "Ti"
    ZI = "Zi"
    EI = "Ei"
    YI = "Yi"


class EnumeratedRootUnitTypeUnit(Enum):
    """
    Attributes:
        METER: The base unit of length in the International System of
            Units (SI).
        GRAM: The base unit of mass in the SI system, defined as one-
            thousandth of a kilogram.
        SECOND: The base unit of time in the SI system.
        AMPERE: The base unit of electric current in the SI system.
        KELVIN: The base unit of thermodynamic temperature in the SI
            system.
        MOLE: The base unit of amount of substance in the SI system.
        CANDELA: The base unit of luminous intensity in the SI system.
        RADIAN: The derived SI unit of angular measure, equal to the
            angle subtended at the center of a circle by an arc whose
            length is equal to the circle’s radius.
        STERADIAN: The SI unit of solid angle measure.
        HERTZ: The SI unit of frequency, defined as one cycle per
            second.
        NEWTON: The SI unit of force, defined as the force required to
            accelerate a one-kilogram mass by one meter per second
            squared.
        PASCAL: The SI unit of pressure, defined as one newton per
            square meter.
        JOULE: The SI unit of energy, defined as one newton-meter.
        WATT: The SI unit of power, defined as one joule per second.
        COULOMB: The coulomb (C) is the SI unit of electric charge,
            defined as the amount of charge transported by a constant
            current of one ampere in one second.
        VOLT: The volt (V) is the SI unit of electric potential and
            electromotive force, defined as the potential difference
            across a conductor when a current of one ampere dissipates
            one watt of power.
        FARAD: The farad (F) is the SI unit of electrical capacitance,
            defined as the ability of a capacitor to store one coulomb
            of charge with a potential difference of one volt.
        OHM: The ohm (Ω) is the SI unit of electrical resistance,
            defined as the resistance between two points of a conductor
            when a voltage of one volt produces a current of one ampere.
        SIEMENS: The siemens (S) is the SI unit of electrical
            conductance, defined as the reciprocal of resistance in
            ohms.
        WEBER: The weber (Wb) is the SI unit of magnetic flux, defined
            as the flux that produces an electromotive force of one volt
            in a circuit with one turn when reduced to zero at a uniform
            rate in one second.
        TESLA: The tesla (T) is the SI unit of magnetic flux density,
            defined as one weber per square meter.
        HENRY: The henry (H) is the SI unit of inductance, defined as
            the inductance of a closed circuit in which an electromotive
            force of one volt is induced when the current changes at a
            rate of one ampere per second.
        DEGREE_CELSIUS: The degree Celsius (°C) is a unit of
            temperature, defined relative to the Kelvin scale, where 0°C
            corresponds to 273.15 K.
        LUMEN: The lumen (lm) is the SI unit of luminous flux, defined
            as the total quantity of visible light emitted by a source
            per unit time.
        LUX: The lux (lx) is the SI unit of illuminance, defined as one
            lumen per square meter.
        KATAL: The katal (kat) is the SI unit of catalytic activity,
            defined as the amount of enzyme activity that converts one
            mole of substrate per second.
        BECQUEREL: The becquerel (Bq) is the SI unit of radioactivity,
            defined as one disintegration per second.
        GRAY: The gray (Gy) is the SI unit of absorbed radiation dose,
            defined as the absorption of one joule of radiation energy
            per kilogram of matter.
        SIEVERT: The sievert (Sv) is the SI unit of equivalent radiation
            dose, used to measure the biological effects of radiation.
        MINUTE: A minute (min) is a unit of time equal to 60 seconds.
        HOUR: An hour (h) is a unit of time equal to 60 minutes or 3600
            seconds.
        DAY: A day (d) is a unit of time equal to 24 hours.
        ARC_DEGREE: An arc degree (°) is a unit of angular measurement,
            equal to 1/360th of a full rotation.
        ARC_MINUTE: An arc minute (′) is a unit of angular measurement,
            equal to 1/60th of a degree.
        ARC_SECOND: An arc second (″) is a unit of angular measurement,
            equal to 1/60th of an arc minute.
        LITER:
        METRIC_TON:
        ELECTRONVOLT:
        UNIFIED_ATOMIC_MASS_UNIT:
        ASTRONOMICAL_UNIT:
        ATOMIC_UNIT_OF_1ST_HYPERPOLARIZABLITY:
        ATOMIC_UNIT_OF_2ND_HYPERPOLARIZABLITY:
        ATOMIC_UNIT_OF_ACTION:
        ATOMIC_UNIT_OF_CHARGE:
        ATOMIC_UNIT_OF_CHARGE_DENSITY:
        ATOMIC_UNIT_OF_CURRENT:
        ATOMIC_UNIT_OF_ELECTRIC_DIPOLE_MOMENT:
        ATOMIC_UNIT_OF_ELECTRIC_FIELD:
        ATOMIC_UNIT_OF_ELECTRIC_FIELD_GRADIENT:
        ATOMIC_UNIT_OF_ELECTRIC_POLARIZABLITY:
        ATOMIC_UNIT_OF_ELECTRIC_POTENTIAL:
        ATOMIC_UNIT_OF_ELECTRIC_QUADRUPOLE_MOMENT:
        ATOMIC_UNIT_OF_ENERGY:
        ATOMIC_UNIT_OF_FORCE:
        ATOMIC_UNIT_OF_LENGTH:
        ATOMIC_UNIT_OF_MAGNETIC_DIPOLE_MOMENT:
        ATOMIC_UNIT_OF_MAGNETIC_FLUX_DENSITY:
        ATOMIC_UNIT_OF_MAGNETIZABILITY:
        ATOMIC_UNIT_OF_MASS:
        ATOMIC_UNIT_OF_MOMENTUM:
        ATOMIC_UNIT_OF_PERMITTIVITY:
        ATOMIC_UNIT_OF_TIME:
        ATOMIC_UNIT_OF_VELOCITY:
        NATURAL_UNIT_OF_ACTION:
        NATURAL_UNIT_OF_ACTION_IN_E_V_S:
        NATURAL_UNIT_OF_ENERGY:
        NATURAL_UNIT_OF_ENERGY_IN_ME_V:
        NATURAL_UNIT_OF_LENGTH:
        NATURAL_UNIT_OF_MASS:
        NATURAL_UNIT_OF_MOMENTUM:
        NATURAL_UNIT_OF_MOMENTUM_IN_ME_V_PER_C:
        NATURAL_UNIT_OF_TIME:
        NATURAL_UNIT_OF_VELOCITY:
        NAUTICAL_MILE:
        KNOT:
        ANGSTROM:
        ARE:
        HECTARE:
        BARN:
        BAR:
        GAL:
        CURIE:
        ROENTGEN:
        RAD:
        REM:
        ERG:
        DYNE:
        BARYE:
        POISE:
        RHE:
        STOKES:
        DARCY:
        KAYSER:
        LAMBERT:
        PHOT:
        THERMO_CALORIE:
        TABLE_CALORIE:
        DEBYE:
        ABAMPERE:
        ABCOULOMB:
        ABFARAD:
        ABHENRY:
        ABOHM:
        ABMHO:
        ABVOLT:
        ABWATT:
        MAXWELL:
        GAUSS:
        GILBERT:
        OERSTED:
        STILB:
        STATAMPERE:
        STATCOULOMB:
        STATFARAD:
        STATHENRY:
        STATOHM:
        STATMHO:
        STATVOLT:
        STATWATT:
        STATWEBER:
        STATTESLA:
        LONG_TON:
        SHORT_TON:
        GROSS_HUNDREDWEIGHT:
        HUNDREDWEIGHT:
        POUND:
        OUNCE:
        DRAM:
        TROY_POUND:
        TROY_OUNCE:
        PENNYWEIGHT:
        APOTHECARIES_DRAM:
        SCRUPLE:
        GRAIN:
        SLUG:
        POUND_FORCE:
        POUNDAL:
        KIP:
        TON_FORCE:
        KILOGRAM_FORCE:
        INCH:
        FOOT:
        YARD:
        MILE:
        US_SURVEY_INCH:
        US_SURVEY_FOOT:
        US_SURVEY_YARD:
        US_SURVEY_FATHOM:
        US_SURVEY_ROD:
        US_SURVEY_CHAIN:
        US_SURVEY_LINK:
        US_SURVEY_FURLONG:
        US_SURVEY_MILE:
        US_ACRE:
        IMPERIAL_GALLON:
        IMPERIAL_QUART:
        IMPERIAL_PINT:
        IMPERIAL_GILL:
        IMPERIAL_OUNCE:
        US_GALLON:
        US_QUART:
        US_PINT:
        US_CUP:
        US_FILL:
        US_FLUID_OUNCE:
        US_FLUID_DRAM:
        US_MINIM:
        US_TABLESPOON:
        US_TEASPOON:
        US_BUSHEL:
        US_PECK:
        US_DRY_QUART:
        US_DRY_PINT:
        THERMO_KG_CALORIE:
        TABLE_KG_CALORIE:
        US_LABEL_TEASPOON:
        US_LABEL_TABLESPOON:
        US_LABEL_CUP:
        US_LABEL_FLUID_OUNCE:
        US_LABEL_OUNCE:
        HORSEPOWER:
        ELECTRIC_HORSEPOWER:
        BOILER_HORSEPOWER:
        METRIC_HORSEPOWER:
        WATER_HORSEPOWER:
        UK_HORSEPOWER:
        DEGREE_FAHRENHEIT:
        DEGREE_RANKINE:
        TORR:
        STANDARD_ATMOSPHERE:
        TECHNICAL_ATMOSPHERE:
        MM_HG:
        CM_HG:
        VALUE_0_C_CM_HG:
        IN_HG:
        VALUE_32_F_IN_HG:
        VALUE_60_F_IN_HG:
        FT_HG:
        MM_WATER:
        CM_WATER:
        VALUE_4_C_CM_WATER:
        IN_WATER:
        VALUE_39_F_IN_WATER:
        VALUE_60_F_IN_WATER:
        FT_WATER:
        VALUE_39_F_FT_WATER:
        LIGHT_YEAR:
        PARSEC:
        PRINTERS_PICA:
        COMPUTER_PICA:
        PRINTERS_POINT:
        COMPUTER_POINT:
        THERMO_BTU:
        TABLE_BTU:
        MEAN_BTU:
        VALUE_39_F_BTU:
        VALUE_59_F_BTU:
        VALUE_60_F_BTU:
        TONS_OF_TNT:
        EC_THERM:
        US_THERM:
        YEAR_365:
        TROPICAL_YEAR:
        SIDEREAL_YEAR:
        SIDEREAL_DAY:
        SIDEREAL_HOUR:
        SIDEREAL_MINUTE:
        SIDEREAL_SECOND:
        SHAKE:
        DENIER:
        TEX:
        GON: A unit of angular measure where one full rotation is
            divided into 400 gons, commonly used in surveying.
        NATO_MIL: A unit of angular measure used in military
            applications, where 1 NATO mil equals 1/6400 of a circle.
        POUND_MOLE: A unit of amount of substance in which the quantity
            is expressed in pounds rather than grams per mole.
        TON_REFRIGERATION: A unit of power used in refrigeration and air
            conditioning, defined as the rate of heat transfer needed to
            freeze 1 short ton (2,000 lb) of water at 32°F in 24 hours.
        CIRCULAR_MIL: A unit of area used in electrical engineering to
            represent wire cross-sectional area, equal to the area of a
            circle with a diameter of one mil (1/1000 inch).
        BEL: A logarithmic unit used to measure ratios, primarily in
            acoustics and electronics; 1 bel equals 10 decibels.
        NEPER: A logarithmic unit used to express ratios, mainly in
            signal processing and acoustics, based on natural
            logarithms.
        P_H: A unitless measure of acidity or alkalinity of a solution,
            defined as the negative logarithm of the hydrogen ion
            concentration.
        PETRO_BARREL: A unit of volume used for crude oil and petroleum
            products, equal to 42 US gallons (approximately 159 liters).
        FOOTLAMBERT: A unit of luminance, defined as 1/π candela per
            square foot.
        FOOTCANDLE: A unit of illuminance, representing the amount of
            light that falls on a surface one foot away from a standard
            candle source.
        CARAT: A unit of mass used for gemstones, equivalent to 200
            milligrams.
    """

    METER = "meter"
    GRAM = "gram"
    SECOND = "second"
    AMPERE = "ampere"
    KELVIN = "kelvin"
    MOLE = "mole"
    CANDELA = "candela"
    RADIAN = "radian"
    STERADIAN = "steradian"
    HERTZ = "hertz"
    NEWTON = "newton"
    PASCAL = "pascal"
    JOULE = "joule"
    WATT = "watt"
    COULOMB = "coulomb"
    VOLT = "volt"
    FARAD = "farad"
    OHM = "ohm"
    SIEMENS = "siemens"
    WEBER = "weber"
    TESLA = "tesla"
    HENRY = "henry"
    DEGREE_CELSIUS = "degree_Celsius"
    LUMEN = "lumen"
    LUX = "lux"
    KATAL = "katal"
    BECQUEREL = "becquerel"
    GRAY = "gray"
    SIEVERT = "sievert"
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    ARC_DEGREE = "arc_degree"
    ARC_MINUTE = "arc_minute"
    ARC_SECOND = "arc_second"
    LITER = "liter"
    METRIC_TON = "metric_ton"
    ELECTRONVOLT = "electronvolt"
    UNIFIED_ATOMIC_MASS_UNIT = "unified_atomic_mass_unit"
    ASTRONOMICAL_UNIT = "astronomical_unit"
    ATOMIC_UNIT_OF_1ST_HYPERPOLARIZABLITY = (
        "atomic_unit_of_1st_hyperpolarizablity"
    )
    ATOMIC_UNIT_OF_2ND_HYPERPOLARIZABLITY = (
        "atomic_unit_of_2nd_hyperpolarizablity"
    )
    ATOMIC_UNIT_OF_ACTION = "atomic_unit_of_action"
    ATOMIC_UNIT_OF_CHARGE = "atomic_unit_of_charge"
    ATOMIC_UNIT_OF_CHARGE_DENSITY = "atomic_unit_of_charge_density"
    ATOMIC_UNIT_OF_CURRENT = "atomic_unit_of_current"
    ATOMIC_UNIT_OF_ELECTRIC_DIPOLE_MOMENT = (
        "atomic_unit_of_electric_dipole_moment"
    )
    ATOMIC_UNIT_OF_ELECTRIC_FIELD = "atomic_unit_of_electric_field"
    ATOMIC_UNIT_OF_ELECTRIC_FIELD_GRADIENT = (
        "atomic_unit_of_electric_field_gradient"
    )
    ATOMIC_UNIT_OF_ELECTRIC_POLARIZABLITY = (
        "atomic_unit_of_electric_polarizablity"
    )
    ATOMIC_UNIT_OF_ELECTRIC_POTENTIAL = "atomic_unit_of_electric_potential"
    ATOMIC_UNIT_OF_ELECTRIC_QUADRUPOLE_MOMENT = (
        "atomic_unit_of_electric_quadrupole_moment"
    )
    ATOMIC_UNIT_OF_ENERGY = "atomic_unit_of_energy"
    ATOMIC_UNIT_OF_FORCE = "atomic_unit_of_force"
    ATOMIC_UNIT_OF_LENGTH = "atomic_unit_of_length"
    ATOMIC_UNIT_OF_MAGNETIC_DIPOLE_MOMENT = (
        "atomic_unit_of_magnetic_dipole_moment"
    )
    ATOMIC_UNIT_OF_MAGNETIC_FLUX_DENSITY = (
        "atomic_unit_of_magnetic_flux_density"
    )
    ATOMIC_UNIT_OF_MAGNETIZABILITY = "atomic_unit_of_magnetizability"
    ATOMIC_UNIT_OF_MASS = "atomic_unit_of_mass"
    ATOMIC_UNIT_OF_MOMENTUM = "atomic_unit_of_momentum"
    ATOMIC_UNIT_OF_PERMITTIVITY = "atomic_unit_of_permittivity"
    ATOMIC_UNIT_OF_TIME = "atomic_unit_of_time"
    ATOMIC_UNIT_OF_VELOCITY = "atomic_unit_of_velocity"
    NATURAL_UNIT_OF_ACTION = "natural_unit_of_action"
    NATURAL_UNIT_OF_ACTION_IN_E_V_S = "natural_unit_of_action_in_eV_s"
    NATURAL_UNIT_OF_ENERGY = "natural_unit_of_energy"
    NATURAL_UNIT_OF_ENERGY_IN_ME_V = "natural_unit_of_energy_in_MeV"
    NATURAL_UNIT_OF_LENGTH = "natural_unit_of_length"
    NATURAL_UNIT_OF_MASS = "natural_unit_of_mass"
    NATURAL_UNIT_OF_MOMENTUM = "natural_unit_of_momentum"
    NATURAL_UNIT_OF_MOMENTUM_IN_ME_V_PER_C = (
        "natural_unit_of_momentum_in_MeV_per_c"
    )
    NATURAL_UNIT_OF_TIME = "natural_unit_of_time"
    NATURAL_UNIT_OF_VELOCITY = "natural_unit_of_velocity"
    NAUTICAL_MILE = "nautical_mile"
    KNOT = "knot"
    ANGSTROM = "angstrom"
    ARE = "are"
    HECTARE = "hectare"
    BARN = "barn"
    BAR = "bar"
    GAL = "gal"
    CURIE = "curie"
    ROENTGEN = "roentgen"
    RAD = "rad"
    REM = "rem"
    ERG = "erg"
    DYNE = "dyne"
    BARYE = "barye"
    POISE = "poise"
    RHE = "rhe"
    STOKES = "stokes"
    DARCY = "darcy"
    KAYSER = "kayser"
    LAMBERT = "lambert"
    PHOT = "phot"
    THERMO_CALORIE = "thermo_calorie"
    TABLE_CALORIE = "table_calorie"
    DEBYE = "debye"
    ABAMPERE = "abampere"
    ABCOULOMB = "abcoulomb"
    ABFARAD = "abfarad"
    ABHENRY = "abhenry"
    ABOHM = "abohm"
    ABMHO = "abmho"
    ABVOLT = "abvolt"
    ABWATT = "abwatt"
    MAXWELL = "maxwell"
    GAUSS = "gauss"
    GILBERT = "gilbert"
    OERSTED = "oersted"
    STILB = "stilb"
    STATAMPERE = "statampere"
    STATCOULOMB = "statcoulomb"
    STATFARAD = "statfarad"
    STATHENRY = "stathenry"
    STATOHM = "statohm"
    STATMHO = "statmho"
    STATVOLT = "statvolt"
    STATWATT = "statwatt"
    STATWEBER = "statweber"
    STATTESLA = "stattesla"
    LONG_TON = "long_ton"
    SHORT_TON = "short_ton"
    GROSS_HUNDREDWEIGHT = "gross_hundredweight"
    HUNDREDWEIGHT = "hundredweight"
    POUND = "pound"
    OUNCE = "ounce"
    DRAM = "dram"
    TROY_POUND = "troy_pound"
    TROY_OUNCE = "troy_ounce"
    PENNYWEIGHT = "pennyweight"
    APOTHECARIES_DRAM = "apothecaries_dram"
    SCRUPLE = "scruple"
    GRAIN = "grain"
    SLUG = "slug"
    POUND_FORCE = "pound_force"
    POUNDAL = "poundal"
    KIP = "kip"
    TON_FORCE = "ton_force"
    KILOGRAM_FORCE = "kilogram_force"
    INCH = "inch"
    FOOT = "foot"
    YARD = "yard"
    MILE = "mile"
    US_SURVEY_INCH = "us_survey_inch"
    US_SURVEY_FOOT = "us_survey_foot"
    US_SURVEY_YARD = "us_survey_yard"
    US_SURVEY_FATHOM = "us_survey_fathom"
    US_SURVEY_ROD = "us_survey_rod"
    US_SURVEY_CHAIN = "us_survey_chain"
    US_SURVEY_LINK = "us_survey_link"
    US_SURVEY_FURLONG = "us_survey_furlong"
    US_SURVEY_MILE = "us_survey_mile"
    US_ACRE = "us_acre"
    IMPERIAL_GALLON = "imperial_gallon"
    IMPERIAL_QUART = "imperial_quart"
    IMPERIAL_PINT = "imperial_pint"
    IMPERIAL_GILL = "imperial_gill"
    IMPERIAL_OUNCE = "imperial_ounce"
    US_GALLON = "us_gallon"
    US_QUART = "us_quart"
    US_PINT = "us_pint"
    US_CUP = "us_cup"
    US_FILL = "us_fill"
    US_FLUID_OUNCE = "us_fluid_ounce"
    US_FLUID_DRAM = "us_fluid_dram"
    US_MINIM = "us_minim"
    US_TABLESPOON = "us_tablespoon"
    US_TEASPOON = "us_teaspoon"
    US_BUSHEL = "us_bushel"
    US_PECK = "us_peck"
    US_DRY_QUART = "us_dry_quart"
    US_DRY_PINT = "us_dry_pint"
    THERMO_KG_CALORIE = "thermo_kg_calorie"
    TABLE_KG_CALORIE = "table_kg_calorie"
    US_LABEL_TEASPOON = "us_label_teaspoon"
    US_LABEL_TABLESPOON = "us_label_tablespoon"
    US_LABEL_CUP = "us_label_cup"
    US_LABEL_FLUID_OUNCE = "us_label_fluid_ounce"
    US_LABEL_OUNCE = "us_label_ounce"
    HORSEPOWER = "horsepower"
    ELECTRIC_HORSEPOWER = "electric_horsepower"
    BOILER_HORSEPOWER = "boiler_horsepower"
    METRIC_HORSEPOWER = "metric_horsepower"
    WATER_HORSEPOWER = "water_horsepower"
    UK_HORSEPOWER = "uk_horsepower"
    DEGREE_FAHRENHEIT = "degree_Fahrenheit"
    DEGREE_RANKINE = "degree_Rankine"
    TORR = "torr"
    STANDARD_ATMOSPHERE = "standard_atmosphere"
    TECHNICAL_ATMOSPHERE = "technical_atmosphere"
    MM_HG = "mm_Hg"
    CM_HG = "cm_Hg"
    VALUE_0_C_CM_HG = "0C_cm_Hg"
    IN_HG = "in_Hg"
    VALUE_32_F_IN_HG = "32F_in_Hg"
    VALUE_60_F_IN_HG = "60F_in_Hg"
    FT_HG = "ft_Hg"
    MM_WATER = "mm_water"
    CM_WATER = "cm_water"
    VALUE_4_C_CM_WATER = "4C_cm_water"
    IN_WATER = "in_water"
    VALUE_39_F_IN_WATER = "39F_in_water"
    VALUE_60_F_IN_WATER = "60F_in_water"
    FT_WATER = "ft_water"
    VALUE_39_F_FT_WATER = "39F_ft_water"
    LIGHT_YEAR = "light_year"
    PARSEC = "parsec"
    PRINTERS_PICA = "printers_pica"
    COMPUTER_PICA = "computer_pica"
    PRINTERS_POINT = "printers_point"
    COMPUTER_POINT = "computer_point"
    THERMO_BTU = "thermo_btu"
    TABLE_BTU = "table_btu"
    MEAN_BTU = "mean_btu"
    VALUE_39_F_BTU = "39F_btu"
    VALUE_59_F_BTU = "59F_btu"
    VALUE_60_F_BTU = "60F_btu"
    TONS_OF_TNT = "tons_of_tnt"
    EC_THERM = "ec_therm"
    US_THERM = "us_therm"
    YEAR_365 = "year_365"
    TROPICAL_YEAR = "tropical_year"
    SIDEREAL_YEAR = "sidereal_year"
    SIDEREAL_DAY = "sidereal_day"
    SIDEREAL_HOUR = "sidereal_hour"
    SIDEREAL_MINUTE = "sidereal_minute"
    SIDEREAL_SECOND = "sidereal_second"
    SHAKE = "shake"
    DENIER = "denier"
    TEX = "tex"
    GON = "gon"
    NATO_MIL = "nato_mil"
    POUND_MOLE = "pound_mole"
    TON_REFRIGERATION = "ton_refrigeration"
    CIRCULAR_MIL = "circular_mil"
    BEL = "bel"
    NEPER = "neper"
    P_H = "pH"
    PETRO_BARREL = "petro_barrel"
    FOOTLAMBERT = "footlambert"
    FOOTCANDLE = "footcandle"
    CARAT = "carat"


@dataclass
class LengthType:
    """
    Type of the quantity length.

    Attributes:
        symbol: Symbol of the quantity length.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="L",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class LuminousIntensityType:
    """
    Type of the quantity luminous intensity.

    Attributes:
        symbol: Symbol of the quantity luminous intensity.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="J",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class MassType:
    """
    Type of the quantity mass.

    Attributes:
        symbol: Symbol of the quantity mass.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="M",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class SymbolType:
    """Type for symbols.

    Used in units, quantities, and prefixes.

    Attributes:
        type_value: Type of symbol representation.  Examples include
            ASCII, unicode, HTML, and MathML.
        content:
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class ThermodynamicTemperatureType:
    """
    Type of the quantity thermodynamic temperature.

    Attributes:
        symbol: Symbol of the quantity thermodynamic temperature.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="Θ",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class TimeType:
    """
    Type of the quantity time.

    Attributes:
        symbol: Symbol of the quantity time.
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    symbol: str = field(
        init=False,
        default="T",
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class ApPos(QuantityT):
    """
    X Position of AP.
    """

    class Meta:
        name = "AP_Pos"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class AirPipeHeight(QuantityT):
    """
    The AirpipeHeight specifies height from the baseline to the top of the air
    pipe, if any.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class AngleOfRepose(QuantityT):
    """
    The natural angle of repose specifies the angle naturally subtended with the
    horizontal by the upper surface of the conic pile, made by the bulk cargo when
    loaded into a hold by a chute using gravity alone.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class AngleTolerance(QuantityT):
    """
    Absolute angular tolerance measure used by the exporting application when
    defining geometry.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ApplicationRefT(ReferenceBaseT):
    class Meta:
        name = "ApplicationRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    external_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Area(QuantityT):
    """
    The bar section area.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ArmLengthU(QuantityT):
    """
    The length of the bracket in local U-direction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ArmLengthV(QuantityT):
    """
    The length of the bracket in local V-direction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Axis(Vector3DT):
    """
    Cylinder revolution axis direction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BaseRadius(QuantityT):
    """
    The radius of the cone at the base.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BlockCoefficient(QuantityT):
    """The block coefficient Cb is the moulded block coefficient corresponding to the waterline at the scantling draught Ts, based on rule length L and moulded breadth B:
    $$C_b=\\frac{Moulded displacement [m^3] at scantling draught T_s}{LBT_s} $$
    Where:
    * B : Greatest moulded breadth, in m, measured amidships at the scantling draught, Ts.
    * Ts : Scantling draught, in m, at which the strength requirements for the scantlings of the ship are met
    and represents the full load condition. The scantling draught is to be not less than that corresponding to the assigned freeboard.(ref. IACS S2 Definition of Ship's Length L and of Block Coefficient Cb - S2.2 Block Coefficient $C_b$)"""

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BuilderInformation(BuilderInformationT):
    """The organization that designs, builds, maintains, and repairs ships.

    This type contains information about the ship, which is specific in
    the context of the shipyard, in which it has been built.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulbAngle(QuantityT):
    """
    Profile width and web thickness.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulbBottomRadius(QuantityT):
    """
    The radius at the bottom of the web.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulbInnerRadius(QuantityT):
    """
    The inner radius of the bulb.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulbOuterRadius(QuantityT):
    """
    The outer radius of the bulb.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulbTopRadius(QuantityT):
    """
    The radius at the top of the bulb.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CarriagePressure(QuantityT):
    """
    The CarriagePressure specifies the required pressure of the compartment in
    which the cargo is to be carried.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CatalogueRefT(ReferenceBaseT):
    """
    Type definition.
    """

    class Meta:
        name = "CatalogueRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class CellRefT(ReferenceBaseT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "CellRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_CELL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Center(Point3DT):
    """
    The centre position of a shape.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CenterOfGravity(Point3DT):
    """The centre of gravity (COG) of the parent object.

    The receiving application can use the value received from the
    authoring application to check that the object has been transferred
    correctly.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ClassNotation(ClassNotationT):
    """
    The notations given to the hull and machinery of the Ship by the classification
    society as a result of its approval activities during the design, manufacture
    and in-service maintenance of the ship (see ISO 10303-218, section 4.2.35).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ConnectionConfigurationRefT(ReferenceBaseT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "ConnectionConfigurationRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_CONNECTION_CONFIGURATION,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ConnectionLength(QuantityT):
    """
    The connection length of the direct connection between a stiffener and a
    primary supporting member.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ContourEnd(Point3DT):
    """
    The end point  of the LimitedBy  contour curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ContourStart(Point3DT):
    """
    The start point  of the LimitedBy  contour curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ControlPointT(Point3DT):
    """
    Attributes:
        weight: The weight associated with the control point. The weight
            is 1.0 if not given (default).
    """

    class Meta:
        name = "ControlPoint_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    weight: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CopeHeight(QuantityT):
    """
    The height of the cope.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CopeLength(QuantityT):
    """The length of the cope.

    (The default is CopeLength=CopeRadius)
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CopeRadius(QuantityT):
    """
    The cope or heel radius.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CurveLength(QuantityT):
    """The curve length computed by the sending application.

    Used to verify geometry reconstruction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CustomPropertyT:
    """
    Type definition.

    Attributes:
        description:
        id:
        name: Property  name.
        value:
        unit:
    """

    class Meta:
        name = "CustomProperty_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    description: Optional[Description] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CutbackDistance(QuantityT):
    """
    Distance from stiffener logical end position to the start of the web cutback.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DeadWeight(QuantityT):
    """
    The weight of the passengers, crew, cargo, stores, ballast, fresh water, fuel
    oil, and other consumables being carried by a ship (see ISO 10303-215, section
    4.2.74).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DeepestEquilibriumWl(QuantityT):
    """
    Deepest equilibrium waterline in damaged condition.
    """

    class Meta:
        name = "DeepestEquilibriumWL"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Density(QuantityT):
    """
    The material density.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DesignSpeed(QuantityT):
    """
    The forward or service speed at which the ship is designed to operate (see ISO
    10303-218, section 4.2.32.2).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Diameter(QuantityT):
    """
    Circle diameter.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Displacement(QuantityT):
    """The Radius displacement outside the original corner of the rectangle.

    If left out (or set to zero), the radius passes through the original
    corner of the rectangle.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DistanceAbove(QuantityT):
    """
    The distance of the lug above the plate (bottom of the slot opening).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DistanceBelow(QuantityT):
    """
    The distance below the lug plate to bottom of the slot.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DistanceToAp(QuantityT):
    """The offset  of  frame zero (#0) from the After Perpendicular (AP).

    The default is zero offset (#0 is located at AP)
    """

    class Meta:
        name = "DistanceToAP"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DistanceTolerance(QuantityT):
    """
    Absolute tolerance measure used by the exporting application when defining
    geometry.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DryWeight(QuantityT):
    """
    The total dry weight of the parent member.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EndCutRefT(ReferenceBaseT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "EndCutRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_END_CUT,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class EndPoint(Point3DT):
    """
    The end position of the segment.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ExternalGeometryRefT:
    class Meta:
        name = "ExternalGeometryRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    external_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    geometry_format: GeometryFormatValue = field(
        init=False,
        default=GeometryFormatValue.STP,
        metadata={
            "name": "geometryFormat",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class FpPos(QuantityT):
    """X-Position of fwd.

    end of waterline for free-board length.
    """

    class Meta:
        name = "FP_Pos"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FilletRadius(QuantityT):
    """
    Corner fillet radius.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FillingHeight(QuantityT):
    """
    The filling_height specifies the maximum height for filling of the tank
    compartment.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlangeCutBackAngle(QuantityT):
    """
    Cut angle of stiffener flange.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlangeDirection(Vector3DT):
    """Direction of the stiffener flange.

    Not required for symmetrical profiles.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlangeNoseHeight(QuantityT):
    """
    Nose height of sniped stiffener flange.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlangeThickness(QuantityT):
    """
    The thickness of the flange.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlangeWidth(QuantityT):
    """
    Section profile flange width.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FreeEdgeRadius(QuantityT):
    """The edge radius at the bracket free edge.

    Assumed to be straight if no radius value is provided.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FreeboardDeckHeight(QuantityT):
    """
    The height of free-board deck, D1.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FreeboardLength(QuantityT):
    """
    The free-board length of the Vessel, Lll.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Header(HeaderT):
    """
    The header information of an XML export.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HeavyBallastDraught(QuantityT):
    """
    The Vessel draught at heavy ballast, Thb.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Height(QuantityT):
    """
    The height of the parent element.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class InertiaU(QuantityT):
    """
    Moment of inertia around NeutralAxisU.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class InertiaV(QuantityT):
    """
    Moment of inertia around NeutralAxisV.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class IntermediatePoint(Point3DT):
    """
    An intermediate point on the circular segment.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class KnotVector(KnotVectorT):
    """The knot-vector is a list of  size m=+n-1 knots where p is the polynomial
    basis degree and n is the number of control points.

    The knot vector consists of a non-decreasing sequence of values.
    Knot multiplicities can be included. A knot multiplicity means that
    a knot value can be repeated up to p+1 times.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LengthOfWaterline(QuantityT):
    """
    The length of the waterline at T, Lwl.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LowerRadius(QuantityT):
    """
    The lower radius of an opening or slot.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Lpp(QuantityT):
    """
    The length of the Vessel between perpendiculars, Lpp.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MajorAxis(Vector3DT):
    """
    Direction of ellipse major axis.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MajorDiameter(QuantityT):
    """
    The ellipse major diameter.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MinorAxis(Vector3DT):
    """
    Definition of the ellipse minor axis direction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MinorDiameter(QuantityT):
    """
    The ellipse minor diameter.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MouldedBreadth(QuantityT):
    """
    The moulded breadth of the Vessel, B.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MouldedDepth(QuantityT):
    """
    The moulded depth of the Vessel, D.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class NurbspropertiesT:
    """
    Type definition of a class defining the properties of the NURBS curve.

    Attributes:
        degree: B-spline degree p is the highest exponent used in the
            polynomial basis function. The B-spline order is always p+1.
            Defined as p = m - n - 1 if not given explicitly where m is
            the number of knots and n is the number of control points.
        num_ctrl_pts: Number of control points in the curve direction or
            the surface grid u or v direction.
        num_knots: numKnots: m=(p+n-1) numbers, where p is the
            polynomial basis degree and n is the number of control
            points.
        form: The NURBS curve form (Open, Closed, or Periodic).
        is_rational: The default is non-rational basis functions
            (isRational=false). Rational refers to the underlying
            mathematical representation. This property allows NURBS to
            represent exact conics (such as parabolic curves, circles,
            and ellipses) in addition to free-form curves. To define
            conical curve types set isRational=true.
    """

    class Meta:
        name = "NURBSProperties_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    num_ctrl_pts: Optional[int] = field(
        default=None,
        metadata={
            "name": "numCtrlPts",
            "type": "Attribute",
            "required": True,
        },
    )
    num_knots: Optional[int] = field(
        default=None,
        metadata={
            "name": "numKnots",
            "type": "Attribute",
            "required": True,
        },
    )
    form: CurveFormEnum = field(
        default=CurveFormEnum.OPEN,
        metadata={
            "type": "Attribute",
        },
    )
    is_rational: bool = field(
        default=False,
        metadata={
            "name": "isRational",
            "type": "Attribute",
        },
    )


@dataclass
class NetArea(QuantityT):
    """The net plate area computed by the sending application.

    The NetArea is the net area of the plate representing the actual plate contour and cut-outs removing material from the plate:
    NetAra*t*density = DryWeight
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class NeutralAxisU(Vector3DT):
    """Position of the neutral axis parallel to the U axis measured from the foot
    point.

    The U axis is along the flange.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class NeutralAxisV(Vector3DT):
    """Position of the neutral axis parallel to the V axis measured from the mould
    line side.

    The V axis is along the web.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Normal(Vector3DT):
    """
    A unit normal vector to a surface.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class NormalBallastDraught(QuantityT):
    """
    The Vessel draught at normal ballast, Tnb.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Offset(QuantityT):
    """An offset from a reference plane or surface.

    A positive offset value is in the direction of the surface normal
    vector.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OffsetU(QuantityT):
    """
    The offset from stiffener trace line of cross-section in local U direction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OffsetV(QuantityT):
    """
    The offset from stiffener trace-line of cross-section in local V direction.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Origin(Point3DT):
    """
    The origin of a local or global coordinate system.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Overshoot(QuantityT):
    """The overshoot of the flange beyond the web.

    Shall be included in the Width..
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Permeability(QuantityT):
    """
    The permeability specifies the amount by which the Cargo takes up water.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Point3D(Point3DT):
    """
    Compact definition of  a point in 3D space composed of  a sequence of three
    double values representing X, Y and Z coordinate values all of the same unit
    given by the unit ID.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PoissonRatio(QuantityT):
    """
    The material Poisson's ration.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Position(Point3DT):
    """
    The position of the inclination of the cross-section.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PrimaryAxis(Vector3DT):
    """
    The unit vector of the local X-axis (U-Axis) given in global Coordinate System.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Quantity(QuantityT):
    """Abstract base class for all types with values carrying a Unit : Q = v * u."""

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Radius(QuantityT):
    """
    The radius of the parent element.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RectangularTubeT:
    """
    Attributes:
        height: Profile outer diameter.
        width: Profile width.
        thickness: Wall thickness.
    """

    class Meta:
        name = "RectangularTube_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    thickness: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ReferenceBase(ReferenceBaseT):
    """
    Abstract type which all reference pointers must inherit from.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ReferenceLocation(QuantityT):
    """
    Location on the reference axis.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ReferencePlane(ReferencePlaneT):
    """
    The concept of a reference plane which is typically used to define an unbounded
    geometry.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ReliefValvePressure(QuantityT):
    """
    Pressure valve opening pressure when exceeding the general value.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RuleLength(QuantityT):
    """The Rule length $L$ is the distance, in metres, measured on the waterline at
    the scantling draught from the fore side of the stem to the after side of the
    rudder post, or the centre of the rudder stock if there is no rudder post.

    $L$ is not to be less than 96%, and need not be greater than 97%, of the extreme length on the waterline at the scantling draught. In ships without rudder stock (e.g. ships fitted with azimuth thrusters), the Rule length $L$ is to be taken equal to 97% of the extreme length on the waterline at the scantling draught. In ships with unusual stern and bow arrangement the Rule length $L$ will be specially considered.(ref. IACS S2 Definition of Ship's Length $L$ and of Block Coefficient $C_b$ - S2.1 Rule Lenght).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ScantlingDraught(QuantityT):
    """Design draught moulded, fully loaded condition, Td.

    The summer load draught used by the classification society in its
    calculations for structural integrity and strength (see ISO
    10303-218, section 4.2.32.6).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SecondaryAxis(Vector3DT):
    """
    The unit vector of the local Y-axis (V-Axis) given in global Coordinate System.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ShipDesignation(ShipDesignationT):
    """The different types of identification given to the ship in order that it can
    be categorised by any shipping related organisation.

    It contains the minimal information which might         be available
    about the ship.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SlammingDraughtEmptyFp(QuantityT):
    """
    The design slamming draught at FP (all ballast tanks empty), Tf-e.
    """

    class Meta:
        name = "SlammingDraughtEmptyFP"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SlammingDraughtFullFp(QuantityT):
    """
    The Vessel draught at FP used when calculation design slamming loads (all
    ballast tanks full), Tf-f.
    """

    class Meta:
        name = "SlammingDraughtFullFP"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SpeedFactor(QuantityT):
    """
    Speed factor Cav.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Start(QuantityT):
    """
    The location of Frame 0 in the frame table.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StartPoint(Point3DT):
    """
    The start position of the segment.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StatutoryData(StatutoryDataT):
    """
    The vessel statutory information.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StowageFactor(QuantityT):
    """The StowageFactor specifies the average specific volume for a dry cargo.

    The stowage factor is usually expressed as the volume in cubic
    meters that is occupied by one metric ton of the cargo.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StowageHeight(QuantityT):
    """Z coordinate of dry bulk stowage height.

    If not specified, top of cargo room will be used.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StructureRefT(ReferenceBaseT):
    """
    Type definition.
    """

    class Meta:
        name = "StructureRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class SweepLength(QuantityT):
    """
    The sweep length used to extrude a surface from a base curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ThermalExpansionCoefficient(QuantityT):
    """
    The material thermal expansion coefficient.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Thickness(QuantityT):
    """
    The thickness of the parent element.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Tip(Point3DT):
    """
    The origin or centre of the cone at the top.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class TipRadius(QuantityT):
    """
    Cone tip radius, use radius =0 if not given.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Tonnage(QuantityT):
    """
    She numerical value resulting from the tonnage calculation (see ISO 10303-215,
    section 4.2.165.3).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class TorsionConstant(QuantityT):
    """
    The torsional constant is calculated from the cross-section and determines the
    torsional rigidity together with the shear modulus.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Udirection(Vector3DT):
    """
    Local U direction in a local coordinate system.
    """

    class Meta:
        name = "UDirection"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UknotVector(KnotVectorT):
    """The knot-vector in U direction is a list of  size m=+n-1 knots where p is
    the polynomial basis degree and n is the number of control points.

    The knot vector consist of a non-decreasing sequence of values. Knot
    multiplicities can be included. A knot multiplicity means that a
    knot value can be repeated up to p+1 times.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UltimateStress(QuantityT):
    """
    The material ultimate stress.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UnitCargoT:
    """
    Type definition of dry cargo properties, reference is made to ISO
    10303-215:2004.
    """

    class Meta:
        name = "UnitCargo_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    unit_cargo_type: Optional[UnitCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "unitCargoType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Unose(QuantityT):
    """
    The bracket nose depth at the local U end of the bracket.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UpperDeckArea(QuantityT):
    """
    Projected area of upper deck forward 0.2 L.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UpperRadius(QuantityT):
    """
    The upper radius of an opening or a slot.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UserDefinedParameterT(QuantityT):
    class Meta:
        name = "UserDefinedParameter_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    description: Optional[Description] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Vdirection(Vector3DT):
    """
    Local V direction in a local coordinate system.
    """

    class Meta:
        name = "VDirection"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Vector3D(Vector3DT):
    """
    Unit vector of length 1.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class VesselRefT(ReferenceBaseT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "VesselRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_VESSEL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class VknotVector(KnotVectorT):
    """The knot-vector in V direction is a list of  size m=+n-1 knots where p is
    the polynomial basis degree and n is the number of control points.

    The knot vector consist of a non-decreasing sequence of values. Knot
    multiplicities can be included. A knot multiplicity means that a
    knot value can be repeated up to p+1 times.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Vnose(QuantityT):
    """
    The bracket nose depth at the local V end of the bracket.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Volume(QuantityT):
    """
    The volume of a compartment or space.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WaterPlaneArea(QuantityT):
    """
    The area of water-plane forward 0.2 L at scantling draught Td.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebCutBackAngle(QuantityT):
    """
    Sniped angle of stiffener web.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebDirection(Vector3DT):
    """
    Direction of the stiffener web.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebNoseHeight(QuantityT):
    """
    Nose height of sniped stiffener web.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebStiffenerRefT(ReferenceBaseT):
    """
    Type definition of WebStiffener connection.

    Attributes:
        position: The position of the web stiffener relative to the
            penetrating stiffener end.
    """

    class Meta:
        name = "WebStiffenerRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    position: Optional[PositionValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class WebThickness(QuantityT):
    """
    The thickness of the web.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Width(QuantityT):
    """
    The width of the parent element.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class X(QuantityT):
    """The X component of a vector or a position.

    The value is a Quantity carrying a unit definition.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Y(QuantityT):
    """The Y component of a vector or a position.

    The value is a Quantity carrying a unit definition.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class YieldStress(QuantityT):
    """
    The material yield stress.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class YoungsModulus(QuantityT):
    """
    The material elasticity modulus.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Z(QuantityT):
    """The Z component of a vector or a position.

    The value is a Quantity carrying a unit definition.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ZposDeckline(QuantityT):
    """
    Vertical distance from baseline to deck-line at FE.
    """

    class Meta:
        name = "ZPosDeckline"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ZposOfDeck(QuantityT):
    """
    Z coordinate of the bulkhead deck.
    """

    class Meta:
        name = "ZPosOfDeck"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class AmountOfSubstance(AmountOfSubstanceType):
    """
    Element containing the dimension of the quantity amount of substance.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class ElectricCurrent(ElectricCurrentType):
    """
    Element containing the dimension of the quantity electric current.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class EnumeratedRootUnitType:
    """Type for the element for a root unit (from an extensive enumerated list)
    allowing an optional prefix and power.

    E.g., mm^2

    Attributes:
        unit: Unit identifier; the enumerated list is basically English
            unit names in lowercase, with a few upper case exceptions,
            e.g., 32F, mmHg, pH.
        source_url: Relevant URL for available information.
        prefix: Prefix identifier; e.g., m, k, M, G.  [Enumeration order
            is by prefix magnitude (Y to y) followed by binary
            prefixes.]
        power_numerator: An integer exponent of the unit.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    unit: Optional[EnumeratedRootUnitTypeUnit] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    source_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceURL",
            "type": "Attribute",
        },
    )
    prefix: Optional[EnumeratedRootUnitTypePrefix] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        },
    )


@dataclass
class Length(LengthType):
    """
    Element containing the dimension of the quantity length.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class LuminousIntensity(LuminousIntensityType):
    """
    Element containing the dimension of the quantity luminous intensity.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class Mass(MassType):
    """
    Element containing the dimension of the quantity mass.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class NameType:
    """Type for name.

    Used for names in units, quantities, and prefixes.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class ThermodynamicTemperature(ThermodynamicTemperatureType):
    """
    Element containing the dimension of the quantity thermodynamic temerature.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class Time(TimeType):
    """
    Element containing the dimension of the quantity time.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class UnitSymbol(SymbolType):
    """Element containing various unit symbols.

    Examples include Aring (ASCII), Å (HTML).
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class ApplicationRef(ApplicationRefT):
    """
    The ApplicationRef element is meant to relate the parent element (Product,
    Representation, etc.) back to the owning entity in the sending application.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BracketRefT(StructureRefT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "BracketRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_BRACKET,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class BulbFlatT:
    """
    BulbFlat type.

    Attributes:
        height: Profile height, measured along the web.
        web_thickness:
        flange_width:
        bulb_angle:
        bulb_outer_radius:
        bulb_inner_radius:
        bulb_top_radius:
        bulb_bottom_radius:
    """

    class Meta:
        name = "BulbFlat_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_width: Optional[FlangeWidth] = field(
        default=None,
        metadata={
            "name": "FlangeWidth",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulb_angle: Optional[BulbAngle] = field(
        default=None,
        metadata={
            "name": "BulbAngle",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulb_outer_radius: Optional[BulbOuterRadius] = field(
        default=None,
        metadata={
            "name": "BulbOuterRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulb_inner_radius: Optional[BulbInnerRadius] = field(
        default=None,
        metadata={
            "name": "BulbInnerRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulb_top_radius: Optional[BulbTopRadius] = field(
        default=None,
        metadata={
            "name": "BulbTopRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulb_bottom_radius: Optional[BulbBottomRadius] = field(
        default=None,
        metadata={
            "name": "BulbBottomRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class BulkCargoT:
    """
    Type definition of dry cargo properties, reference is made to ISO
    10303-215:2004.
    """

    class Meta:
        name = "BulkCargo_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    stowage_factor: Optional[StowageFactor] = field(
        default=None,
        metadata={
            "name": "StowageFactor",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    permeability: Optional[Permeability] = field(
        default=None,
        metadata={
            "name": "Permeability",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    angle_of_repose: Optional[AngleOfRepose] = field(
        default=None,
        metadata={
            "name": "AngleOfRepose",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulk_cargo_type: Optional[BulkCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "bulkCargoType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class CatalogueRef(CatalogueRefT):
    """
    A reference to a catalogue item.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CellRef(CellRefT):
    """
    A reference to a Compartment cell.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CompartmentPropertiesT:
    """
    Type definition of the physical properties of a compartment volume (COG, air
    pipe top).

    Attributes:
        center_of_gravity: COG of the closed space.
        volume:
        air_pipe_height:
        filling_height: The filling height specifies the maximum height
            for filling of the tank compartment.
        relief_valve_pressure:
    """

    class Meta:
        name = "CompartmentProperties_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    center_of_gravity: Optional[CenterOfGravity] = field(
        default=None,
        metadata={
            "name": "CenterOfGravity",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    volume: Optional[Volume] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    air_pipe_height: Optional[AirPipeHeight] = field(
        default=None,
        metadata={
            "name": "AirPipeHeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    filling_height: Optional[FillingHeight] = field(
        default=None,
        metadata={
            "name": "FillingHeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    relief_valve_pressure: Optional[ReliefValvePressure] = field(
        default=None,
        metadata={
            "name": "ReliefValvePressure",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class ConnectionConfigurationRef(ConnectionConfigurationRefT):
    """
    A reference to the the a stiffener connection configuration.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ContourBoundsT:
    """
    The type definition of the ContourBounds.
    """

    class Meta:
        name = "ContourBounds_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    contour_start: Optional[ContourStart] = field(
        default=None,
        metadata={
            "name": "ContourStart",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    contour_end: Optional[ContourEnd] = field(
        default=None,
        metadata={
            "name": "ContourEnd",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ControlPoint(ControlPointT):
    """
    A NURBS control point composed of a weight and spatial position.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CustomProperty(CustomPropertyT):
    """
    A generic custom property type with a key, value pair and optional unit.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DocumentBaseT:
    """
    Type definition of the abstract base class for the XML document defined in this
    schema.

    Attributes:
        header:
        schema_version: Current XML schema version (Format - x.y.z) x :
            Incremented for backward incompatible changes ( Ex - Adding
            a required attribute, etc.) y : Major backward compatible
            changes [ Ex - Adding a new node ,fixing major CRs,etc...] z
            : Minor backward compatible changes (Ex - adding an optional
            attribute, etc).
        language: Language used by the application.
    """

    class Meta:
        name = "DocumentBase_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    header: Optional[Header] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    schema_version: str = field(
        init=False,
        default="3.1.0",
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )
    language: str = field(
        default="en",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EndCutRef(EndCutRefT):
    """
    A reference to the Stiffener end cut detail.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ExternalGeometryRef(ExternalGeometryRefT):
    """
    The ExternalGeometryRef element is used to point to an external geometry
    representation of the parent entity (e.g. Plate, Stiffener, Bracket, Member).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FeatureCopeT:
    """
    Cope parameters.

    Attributes:
        cope_radius:
        cope_length: The length of the cope measured along the stiffener
            trace-line (X-axis)  from the end of the stiffener to the
            centre of the cope radius.
        cope_height: The height of the cope measured along the cross
            section local V-direction from the root point to the centre
            of the cope radius.
    """

    class Meta:
        name = "FeatureCope_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    cope_radius: Optional[CopeRadius] = field(
        default=None,
        metadata={
            "name": "CopeRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    cope_length: Optional[CopeLength] = field(
        default=None,
        metadata={
            "name": "CopeLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cope_height: Optional[CopeHeight] = field(
        default=None,
        metadata={
            "name": "CopeHeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class FlangeEdgeReinforcementT:
    """
    Attributes:
        flange_width: The width of the bracket flange edge
            reinforcement.
        radius: The bend radius of the transition zone between bracket
            web and bracket flange.
    """

    class Meta:
        name = "FlangeEdgeReinforcement_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    flange_width: Optional[FlangeWidth] = field(
        default=None,
        metadata={
            "name": "FlangeWidth",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class FlatBarT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
    """

    class Meta:
        name = "FlatBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class GaseousCargoT:
    """
    Type definition of  Liquid cargo physical properties.

    Attributes:
        density: The density specifies the  of  cargo density.
        carriage_pressure:
        liquid_state: Set to True if the gaseous cargo is carried in a
            liquid state.
        liquid_cargo_type: The liquid cargo types after ISO
            10303-215:2004.
    """

    class Meta:
        name = "GaseousCargo_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    density: Optional[Density] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    carriage_pressure: Optional[CarriagePressure] = field(
        default=None,
        metadata={
            "name": "CarriagePressure",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    liquid_state: bool = field(
        default=False,
        metadata={
            "name": "liquidState",
            "type": "Attribute",
        },
    )
    liquid_cargo_type: Optional[LiquidCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "liquidCargoType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class HalfRoundBarT:
    """
    Attributes:
        diameter: The HalfRoundBar diameter. The HalfRoundBar height is
            D/2
    """

    class Meta:
        name = "HalfRoundBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    diameter: Optional[Diameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class HexagonBarT:
    """
    Attributes:
        height: The profile height.
    """

    class Meta:
        name = "HexagonBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class HoleContourRefT(StructureRefT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "HoleContourRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_HOLE2_DCONTOUR,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class HoleRefT(CatalogueRefT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "HoleRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_HOLE2_D,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class IbarT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """

    class Meta:
        name = "IBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class InclinationT:
    """
    Type definition of inclination of stiffener or member along its trace line (web
    and flange directions).
    """

    class Meta:
        name = "Inclination_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    web_direction: Optional[WebDirection] = field(
        default=None,
        metadata={
            "name": "WebDirection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_direction: Optional[FlangeDirection] = field(
        default=None,
        metadata={
            "name": "FlangeDirection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class LbarOfT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness: Thickness of the web.
        flange_thickness: Thickness of the flange.
        overshoot:
    """

    class Meta:
        name = "LBarOF_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    overshoot: Optional[Overshoot] = field(
        default=None,
        metadata={
            "name": "Overshoot",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class LbarOwT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
        overshoot: Overshoot of the web above the flange. Should be
            added to the Height to get the total height.
    """

    class Meta:
        name = "LBarOW_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    overshoot: Optional[Overshoot] = field(
        default=None,
        metadata={
            "name": "Overshoot",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class LbarT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """

    class Meta:
        name = "LBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class LiquidCargoT:
    """
    Type definition of  Liquid cargo physical properties.

    Attributes:
        density: The density of  ballast, bunker or liquid cargo
            content.
        carriage_pressure:
        liquid_cargo_type:
    """

    class Meta:
        name = "LiquidCargo_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    density: Optional[Density] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    carriage_pressure: Optional[CarriagePressure] = field(
        default=None,
        metadata={
            "name": "CarriagePressure",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    liquid_cargo_type: Optional[LiquidCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "liquidCargoType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class LugPlaterRefT(StructureRefT):
    """
    Type definition.

    Attributes:
        connection_length: Length of lug plate connection welded to
            stiffener web.
        distance_above:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "LugPlaterRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    connection_length: Optional[ConnectionLength] = field(
        default=None,
        metadata={
            "name": "ConnectionLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    distance_above: Optional[DistanceAbove] = field(
        default=None,
        metadata={
            "name": "DistanceAbove",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PLATE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class MaterialRefT(CatalogueRefT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "MaterialRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_MATERIAL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Nurbsproperties(NurbspropertiesT):
    """
    Properties of the basis functions in surface V direction.
    """

    class Meta:
        name = "NURBSproperties"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OctagonBarT:
    """
    Attributes:
        height: Profile height and width measured as the distance
            between two parallel sides.
    """

    class Meta:
        name = "OctagonBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PhysicalPropertiesT:
    """
    Type definition of physical properties of structure objects (weight and centre
    of gravity).
    """

    class Meta:
        name = "PhysicalProperties_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    dry_weight: Optional[DryWeight] = field(
        default=None,
        metadata={
            "name": "DryWeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    center_of_gravity: Optional[CenterOfGravity] = field(
        default=None,
        metadata={
            "name": "CenterOfGravity",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PillarRefT(StructureRefT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "PillarRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PILLAR,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PlateMaterialRefT(CatalogueRefT):
    """
    Type definition.

    Attributes:
        thickness:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "PlateMaterialRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_MATERIAL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PlateRefT(StructureRefT):
    """
    Type definition.

    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "PlateRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PLATE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PositionsT:
    class Meta:
        name = "Positions_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    point3_d: list[Point3D] = field(
        default_factory=list,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 3,
            "max_occurs": 3,
        },
    )


@dataclass
class PrincipalParticularsT:
    """
    Type definition of the  main vessel particulars required by the Society.

    Attributes:
        lpp:
        rule_length:
        block_coefficient:
        fp_pos:
        moulded_breadth:
        moulded_depth:
        scantling_draught:
        design_speed:
        freeboard_length:
        normal_ballast_draught:
        heavy_ballast_draught:
        slamming_draught_empty_fp:
        slamming_draught_full_fp:
        length_of_waterline:
        freeboard_deck_height:
        ap_pos:
        zpos_of_deck:
        deepest_equilibrium_wl:
        upper_deck_area:
        water_plane_area:
        zpos_deckline:
        speed_factor:
        has_deadweight_less_than: The ship has dead-weight less than
            50000 tonnes (boolean).
        has_bilge_keel: Whether the vessel has a bilge keel or not.
        freeboard_type: Enumerated free-board types according to the
            Rules. Type A ship is one which:— is designed to carry only
            liquid cargoes in bulk has a high integrity of the exposed
            deck with only small access openings to cargo compartments,
            closed by watertight gasket covers of steel or equivalent
            material has low permeability of loaded cargo compartments.
            All ships which are not Type A ships shall be considered as
            Type B ships.                                         .
        number_of_decks_above: Number of decks above 0.7 D from
            baseline.
    """

    class Meta:
        name = "PrincipalParticulars_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    lpp: Optional[Lpp] = field(
        default=None,
        metadata={
            "name": "Lpp",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    rule_length: Optional[RuleLength] = field(
        default=None,
        metadata={
            "name": "RuleLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    block_coefficient: Optional[BlockCoefficient] = field(
        default=None,
        metadata={
            "name": "BlockCoefficient",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    fp_pos: Optional[FpPos] = field(
        default=None,
        metadata={
            "name": "FP_Pos",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    moulded_breadth: Optional[MouldedBreadth] = field(
        default=None,
        metadata={
            "name": "MouldedBreadth",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    moulded_depth: Optional[MouldedDepth] = field(
        default=None,
        metadata={
            "name": "MouldedDepth",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    scantling_draught: Optional[ScantlingDraught] = field(
        default=None,
        metadata={
            "name": "ScantlingDraught",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    design_speed: Optional[DesignSpeed] = field(
        default=None,
        metadata={
            "name": "DesignSpeed",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    freeboard_length: Optional[FreeboardLength] = field(
        default=None,
        metadata={
            "name": "FreeboardLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    normal_ballast_draught: Optional[NormalBallastDraught] = field(
        default=None,
        metadata={
            "name": "NormalBallastDraught",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    heavy_ballast_draught: Optional[HeavyBallastDraught] = field(
        default=None,
        metadata={
            "name": "HeavyBallastDraught",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    slamming_draught_empty_fp: Optional[SlammingDraughtEmptyFp] = field(
        default=None,
        metadata={
            "name": "SlammingDraughtEmptyFP",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    slamming_draught_full_fp: Optional[SlammingDraughtFullFp] = field(
        default=None,
        metadata={
            "name": "SlammingDraughtFullFP",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    length_of_waterline: Optional[LengthOfWaterline] = field(
        default=None,
        metadata={
            "name": "LengthOfWaterline",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    freeboard_deck_height: Optional[FreeboardDeckHeight] = field(
        default=None,
        metadata={
            "name": "FreeboardDeckHeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ap_pos: Optional[ApPos] = field(
        default=None,
        metadata={
            "name": "AP_Pos",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    zpos_of_deck: Optional[ZposOfDeck] = field(
        default=None,
        metadata={
            "name": "ZPosOfDeck",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    deepest_equilibrium_wl: Optional[DeepestEquilibriumWl] = field(
        default=None,
        metadata={
            "name": "DeepestEquilibriumWL",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    upper_deck_area: Optional[UpperDeckArea] = field(
        default=None,
        metadata={
            "name": "UpperDeckArea",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    water_plane_area: Optional[WaterPlaneArea] = field(
        default=None,
        metadata={
            "name": "WaterPlaneArea",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    zpos_deckline: Optional[ZposDeckline] = field(
        default=None,
        metadata={
            "name": "ZPosDeckline",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    speed_factor: Optional[SpeedFactor] = field(
        default=None,
        metadata={
            "name": "SpeedFactor",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    has_deadweight_less_than: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasDeadweightLessThan",
            "type": "Attribute",
        },
    )
    has_bilge_keel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasBilgeKeel",
            "type": "Attribute",
        },
    )
    freeboard_type: FreeboardTypeValue = field(
        default=FreeboardTypeValue.A,
        metadata={
            "name": "freeboardType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    number_of_decks_above: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfDecksAbove",
            "type": "Attribute",
        },
    )


@dataclass
class RectangularTube(RectangularTubeT):
    """
    Rectangular tube.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RoundBarT:
    """
    Attributes:
        height: Profile diameter.
    """

    class Meta:
        name = "RoundBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SectionPropertiesT:
    """
    Generic bar section properties.

    Attributes:
        area: Cross-section area.
        neutral_axis_u:
        neutral_axis_v:
        inertia_u:
        inertia_v:
        torsion_constant:
    """

    class Meta:
        name = "SectionProperties_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    area: Optional[Area] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    neutral_axis_u: Optional[NeutralAxisU] = field(
        default=None,
        metadata={
            "name": "NeutralAxisU",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    neutral_axis_v: Optional[NeutralAxisV] = field(
        default=None,
        metadata={
            "name": "NeutralAxisV",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    inertia_u: Optional[InertiaU] = field(
        default=None,
        metadata={
            "name": "InertiaU",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    inertia_v: Optional[InertiaV] = field(
        default=None,
        metadata={
            "name": "InertiaV",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    torsion_constant: Optional[TorsionConstant] = field(
        default=None,
        metadata={
            "name": "TorsionConstant",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class SectionRefT(CatalogueRefT):
    """
    Type definition.

    Attributes:
        offset_u:
        offset_v:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "SectionRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    offset_u: Optional[OffsetU] = field(
        default=None,
        metadata={
            "name": "OffsetU",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    offset_v: Optional[OffsetV] = field(
        default=None,
        metadata={
            "name": "OffsetV",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_BAR_SECTION,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SquareBarT:
    """
    Attributes:
        height: Profile height, measured along the web.
    """

    class Meta:
        name = "SquareBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class StructureRef(StructureRefT):
    """
    Collection of references to physical structure parts with a geometry.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SweepT:
    """
    Type definition of a sweep extent defined by a direction and length.

    Attributes:
        vector3_d: The sweep direction given by a Unit vector of length
            1.
        sweep_length: The extent of the sweep.
    """

    class Meta:
        name = "Sweep_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    vector3_d: Optional[Vector3D] = field(
        default=None,
        metadata={
            "name": "Vector3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    sweep_length: Optional[SweepLength] = field(
        default=None,
        metadata={
            "name": "SweepLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class TbarT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """

    class Meta:
        name = "TBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class TonnageDataT:
    """
    The information pertinent to the tonnage of the ship.
    """

    class Meta:
        name = "TonnageData_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    tonnage: Optional[Tonnage] = field(
        default=None,
        metadata={
            "name": "Tonnage",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    dead_weight: Optional[DeadWeight] = field(
        default=None,
        metadata={
            "name": "DeadWeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class TransformationT:
    """
    Type definition for a Local (Orthogonal) Axis System.
    """

    class Meta:
        name = "Transformation_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    primary_axis: Optional[PrimaryAxis] = field(
        default=None,
        metadata={
            "name": "PrimaryAxis",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    secondary_axis: Optional[SecondaryAxis] = field(
        default=None,
        metadata={
            "name": "SecondaryAxis",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class TubeT:
    """
    Attributes:
        diameter: The tube diameter.
        thickness:
    """

    class Meta:
        name = "Tube_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    diameter: Optional[Diameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class UbarT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """

    class Meta:
        name = "UBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class UNurbsproperties(NurbspropertiesT):
    """
    Properties of the basis functions in surface U direction.
    """

    class Meta:
        name = "U_NURBSproperties"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UnitCargo(UnitCargoT):
    """The UnitCargo type is intended for spaces carrying a type of dry cargo that
    that is packed or comprises discrete units that can be loaded and stored
    individually on the ship.

    Ref. is made to ISO 10303-215:2004.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UserDefinedParameter(UserDefinedParameterT):
    """
    A user-defined parameter which can be provided to define a user-defined
    BarSection.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class VNurbsproperties(NurbspropertiesT):
    """
    Properties of the basis functions in surface V direction.
    """

    class Meta:
        name = "V_NURBSproperties"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class VesselRef(VesselRefT):
    """
    A reference to the the Vessel.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ZbarT:
    """
    Attributes:
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """

    class Meta:
        name = "ZBar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class DimensionType:
    """
    Type for dimension.

    Attributes:
        length:
        mass:
        time:
        electric_current:
        thermodynamic_temperature:
        amount_of_substance:
        luminous_intensity:
        id:
        dimensionless: Boolean to designate that a quantity or unit is
            dimensionless.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    length: list[Length] = field(
        default_factory=list,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    mass: list[Mass] = field(
        default_factory=list,
        metadata={
            "name": "Mass",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    time: list[Time] = field(
        default_factory=list,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    electric_current: list[ElectricCurrent] = field(
        default_factory=list,
        metadata={
            "name": "ElectricCurrent",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    thermodynamic_temperature: list[ThermodynamicTemperature] = field(
        default_factory=list,
        metadata={
            "name": "ThermodynamicTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    amount_of_substance: list[AmountOfSubstance] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfSubstance",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    luminous_intensity: list[LuminousIntensity] = field(
        default_factory=list,
        metadata={
            "name": "LuminousIntensity",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    dimensionless: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EnumeratedRootUnit(EnumeratedRootUnitType):
    """Element for a root unit (from an extensive enumerated list) allowing an
    optional prefix and power.

    E.g., mm^2
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class UnitName(NameType):
    """
    Element containing the unit name.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class BracketRef(BracketRefT):
    """
    A  reference to a Bracket instance.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulbFlat(BulbFlatT):
    """
    Bulb bar, rolled or welded.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BulkCargo(BulkCargoT):
    """A bulk cargo is a type of dry cargo that is solid cargo that is not packed,
    but is carried loose.

    Ref. is made to ISO 10303-215:2004.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CellConnectionT:
    """
    Type definition for connecting cells to a compartment.

    Attributes:
        cell_ref: A reference to the two connected compartment cells.
    """

    class Meta:
        name = "CellConnection_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    cell_ref: list[CellRef] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass
class CompartmentProperties(CompartmentPropertiesT):
    """
    The physical properties of a compartment volume (COG, air pipe top).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ConnectedBracketRef(BracketRefT):
    """
    The reference to a connected bracket part of a ConnectionConfiguration.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    position: Optional[PositionValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class ContourBounds(ContourBoundsT):
    """
    The definition of a contour bound.The contour bound defines the contour curve
    start and end points.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ControlPtListT:
    """
    Type definition.

    Attributes:
        control_point: The number of control points mist be minimum 2.
            The control point is composed of point in 3D space and an
            optional weight.
    """

    class Meta:
        name = "ControlPtList_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    control_point: list[ControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "ControlPoint",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 2,
        },
    )


@dataclass
class CustomPropertiesT:
    class Meta:
        name = "CustomProperties_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    custom_property: list[CustomProperty] = field(
        default_factory=list,
        metadata={
            "name": "CustomProperty",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class DocumentBase(DocumentBaseT):
    """
    Abstract base class for the XML document defined in this schema.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FeatureCope(FeatureCopeT):
    """
    Parameters of cope features defining additional bracket or stiffener end cut
    details.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlangeEdgeReinforcement(FlangeEdgeReinforcementT):
    """
    Bracket flange edge reinforcement parameters.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FlatBar(FlatBarT):
    """
    Flat bar, rolled or cut from plate.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class GaseousCargo(GaseousCargoT):
    """Liquid cargo properties, reference is made to ISO 10303-215:2004.

    A Gaseous cargo is a type of Cargo that has a natural condition of a
    non-solid, non-liquid gaseous state.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HalfRoundBar(HalfRoundBarT):
    """
    Half round bar.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HexagonBar(HexagonBarT):
    """
    A symmetrical hexagon shaped bar.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HoleContourRef(HoleContourRefT):
    """
    A reference to a catalogue 2D hole contour.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HoleRef(HoleRefT):
    """
    A reference to a catalogue 2D hole.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Ibar(IbarT):
    """
    I-section bar, rolled or welded.
    """

    class Meta:
        name = "IBar"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Inclination(InclinationT):
    """The inclination of the cross-section of a stiffener or a pillar along its
    trace line.

    A vector pair giving the local orientation of the web and flange
    directions at the point given by the Position element. The
    FlangeDirection is optional and not necessary for a symmetrical
    cross-section. Only one inclination is necessary for a non-twisted
    (straight) stiffener or pillar.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Lbar(LbarT):
    """
    An angle bar, rolled or welded.
    """

    class Meta:
        name = "LBar"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LbarOf(LbarOfT):
    """
    Welded angle bar where the flange has an overshoot beyond the web.
    """

    class Meta:
        name = "LBarOF"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LbarOw(LbarOwT):
    """
    Welded angle bar where the web has an overshoot above the flange.
    """

    class Meta:
        name = "LBarOW"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LiquidCargo(LiquidCargoT):
    """Liquid cargo properties, reference is made to ISO 10303-215:2004.

    A liquid cargo is a type of Cargo whose natural condition is a non-
    solid, non-gaseous liquid state.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LocalCartesian(TransformationT):
    """To specify a Local (Orthogonal) Axis System Origin and two of the local
    X,Y,Z axis need to be specified.

    When used to specify a Plane the XY (UV) plane is considered.
    Optional if the coordinate system is referring to the global
    coordinate frame (world coordinates)
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LugPlateRef(LugPlaterRefT):
    """
    The reference to plate lugs with additional lug parameters.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MaterialRef(MaterialRefT):
    """
    A reference to a material in the catalogue.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OctagonBar(OctagonBarT):
    """
    An octagon shaped bar.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PhysicalProperties(PhysicalPropertiesT):
    """Basic physical properties of structure objects (weight and centre of
    gravity).

    These properties are provided by the exporting application and can
    be used as a quality measure by the receiving application to ensure
    correctness of the import.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PillarRef(PillarRefT):
    """
    The reference to a connected Member (Pillar).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PlateMaterial(PlateMaterialRefT):
    """
    Definition of the Plate material and plate thickness.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PlateRef(PlateRefT):
    """
    The reference to a connected Plate.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Positions(PositionsT):
    """
    3 3D-Points defining the circum circle.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PrincipalParticulars(PrincipalParticularsT):
    """
    Main vessel particulars required by the Society.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RoundBar(RoundBarT):
    """
    Round bar.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SectionProperties(SectionPropertiesT):
    """
    Generic bar section properties.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SectionRef(SectionRefT):
    """
    A reference to the parents cross-section.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SquareBar(SquareBarT):
    """
    Square bar.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Sweep(SweepT):
    """
    Definition of the sweep extent  by a direction and sweep  length.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Tbar(TbarT):
    """
    T-section bar, rolled or welded.
    """

    class Meta:
        name = "TBar"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class TonnageData(TonnageDataT):
    """
    The Vessel tonnage information.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Transformation(TransformationT):
    """A concept specifying a local (orthogonal) axis system.

    The Origin and two of the local X,Y,Z axis have to be specified.
    When used to specify a Plane the XY (UV) plane is considered. The
    third axis is found by the cross product of the primary and
    secondary axis.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Tube(TubeT):
    """
    Circular tube.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Ubar(UbarT):
    """
    U-section bar, rolled or welded.
    """

    class Meta:
        name = "UBar"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Zbar(ZbarT):
    """
    Z-section bar, rolled or welded.
    """

    class Meta:
        name = "ZBar"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Dimension(DimensionType):
    """
    Element to express the dimension of a unit or quantity in terms of the SI base
    quantities length, mass, time, electric current, thermodynamic temperature,
    amount of substance, and luminous intensity.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class RootUnitsType:
    """Type for the container for defining derived units in terms of their root
    units.

    This allows a precise definition of a wide range of units. The goal
    is to improve interoperability among applications and databases
    which use derived units based on commonly encountered base units.

    Attributes:
        enumerated_root_unit: Element for a root unit (from an extensive
            enumerated list) allowing an optional prefix and power.
            E.g., mm^2
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    enumerated_root_unit: list[EnumeratedRootUnit] = field(
        default_factory=list,
        metadata={
            "name": "EnumeratedRootUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        },
    )


@dataclass
class BoundedRefT(ReferenceBaseT):
    """
    Type description.
    """

    class Meta:
        name = "BoundedRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    contour_bounds: Optional[ContourBounds] = field(
        default=None,
        metadata={
            "name": "ContourBounds",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class BracketParametersT:
    """
    Type definition of Common parameters defining bracket configurations used in
    shipbuilding.

    Attributes:
        arm_length_u:
        arm_length_v:
        udirection: Local U direction of the Bracket
        vdirection: Local V direction of the Bracket.
        origin: The origin or root point of the Bracket
        unose:
        vnose:
        free_edge_radius:
        feature_cope:
        flange_edge_reinforcement:
        has_edge_reinforcement:
        number_of_supports: Number of supported (welded) bracket edges.
        reinforcement_type:
    """

    class Meta:
        name = "BracketParameters_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    arm_length_u: Optional[ArmLengthU] = field(
        default=None,
        metadata={
            "name": "ArmLengthU",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    arm_length_v: Optional[ArmLengthV] = field(
        default=None,
        metadata={
            "name": "ArmLengthV",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    udirection: Optional[Udirection] = field(
        default=None,
        metadata={
            "name": "UDirection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    vdirection: Optional[Vdirection] = field(
        default=None,
        metadata={
            "name": "VDirection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    unose: Optional[Unose] = field(
        default=None,
        metadata={
            "name": "Unose",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    vnose: Optional[Vnose] = field(
        default=None,
        metadata={
            "name": "Vnose",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    free_edge_radius: Optional[FreeEdgeRadius] = field(
        default=None,
        metadata={
            "name": "FreeEdgeRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    feature_cope: Optional[FeatureCope] = field(
        default=None,
        metadata={
            "name": "FeatureCope",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    flange_edge_reinforcement: Optional[FlangeEdgeReinforcement] = field(
        default=None,
        metadata={
            "name": "FlangeEdgeReinforcement",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    has_edge_reinforcement: bool = field(
        default=False,
        metadata={
            "name": "hasEdgeReinforcement",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    number_of_supports: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSupports",
            "type": "Attribute",
        },
    )
    reinforcement_type: Optional[ReinforcementTypeValue] = field(
        default=None,
        metadata={
            "name": "reinforcementType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class CellConnection(CellConnectionT):
    """
    Cross flow connection between two cells.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ClassDataT:
    """
    Type definition of the main vessel data including Class Notation required by
    the Classification Society.

    Attributes:
        principal_particulars: Information that specifies design and
            intended performance characteristics of the ship in
            accordance with classification society rules and statutory
            regulations (see ISO 10303-218, section 4.2.36).
        class_notation:
        newbuilding_society:
        identification: The classification society specific identifier
            to a ship, typically the design ID.
        newbuilding_society_name: The common name of the class society
            relevant for operating the ship. Needs only to be specified
            when @newbuildingSociety = OTHER
            .
        society:
        society_name: The common name of the class society relevant for
            operating the ship. Needs only to be specified when @society
            = OTHER                            .
    """

    class Meta:
        name = "ClassData_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    principal_particulars: Optional[PrincipalParticulars] = field(
        default=None,
        metadata={
            "name": "PrincipalParticulars",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    class_notation: Optional[ClassNotation] = field(
        default=None,
        metadata={
            "name": "ClassNotation",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    newbuilding_society: Optional[ClassificationSociety] = field(
        default=None,
        metadata={
            "name": "newbuildingSociety",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    identification: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    newbuilding_society_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "newbuildingSocietyName",
            "type": "Attribute",
        },
    )
    society: Optional[ClassificationSociety] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    society_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "societyName",
            "type": "Attribute",
        },
    )


@dataclass
class ControlPtList(ControlPtListT):
    """List of control points (X,Y,Z) and their optional weights.

    The array length N=degree+1. A minimum of 2 control points is
    necessary to define a curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CustomProperties(CustomPropertiesT):
    """
    Container for custom properties.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DoubleBracketT:
    """
    Type definition of DoubleBracket connection.

    Attributes:
        connected_bracket_ref: The reference to a connected bracket part
            of a ConnectionConfiguration. For a double bracket
            connection type, two references must be provided.
    """

    class Meta:
        name = "DoubleBracket_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    connected_bracket_ref: list[ConnectedBracketRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass
class SingleBracketT:
    """
    Type definition of DoubleBracket connection.
    """

    class Meta:
        name = "SingleBracket_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    connected_bracket_ref: Optional[ConnectedBracketRef] = field(
        default=None,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SlotParametersT:
    """
    Type definition of the SlotParameters for a slot cut-out typically used in
    shipbuilding.

    Attributes:
        height: The height of the slot.
        width: The width of the slot.
        upper_radius: Upper radius of slot opening.
        connection_length:
        lower_radius: Lower radius of slot opening.
        lug_plate_ref: Reference to collar or plate lugs welded to the
            stiffener.
        asymmetric:
        slot_type:
    """

    class Meta:
        name = "SlotParameters_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    upper_radius: Optional[UpperRadius] = field(
        default=None,
        metadata={
            "name": "UpperRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    connection_length: Optional[ConnectionLength] = field(
        default=None,
        metadata={
            "name": "ConnectionLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    lower_radius: Optional[LowerRadius] = field(
        default=None,
        metadata={
            "name": "LowerRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    lug_plate_ref: list[LugPlateRef] = field(
        default_factory=list,
        metadata={
            "name": "LugPlateRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "max_occurs": 2,
        },
    )
    asymmetric: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    slot_type: SlotTypeValue = field(
        default=SlotTypeValue.OPEN,
        metadata={
            "name": "slotType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class DimensionSetType:
    """
    Type for the dimension container.

    Attributes:
        dimension: Element to express a unit or quantity in terms of the
            SI base quantities length, mass, time, electric current,
            thermodynamic temperature, amount of substance, and luminous
            intensity.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    dimension: list[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "min_occurs": 1,
        },
    )


@dataclass
class RootUnits(RootUnitsType):
    """Container for defining derived units in terms of their root units.

    This allows a precise definition of a wide range of units. The goal
    is to improve interoperability among applications and databases
    which use derived units based on commonly encountered root units.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class BoundedRef(BoundedRefT):
    """A collection of references  to object with geometry that can be used to
    limit an object.

    ContourBounds can be added to aid resolving the closed contour
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BracketParameters(BracketParametersT):
    """
    Bracket parameters necessary for the verification by the society.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CellBoundaryT(BoundedRefT):
    """
    Attributes:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "CellBoundary_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PANEL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ClassificationData(ClassDataT):
    """
    Information that specifies design and intended performance characteristics of
    the ship in accordance with classification society rules and statutory
    regulations (see ISO       10303-218, section 4.2.36).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DoubleBracket(DoubleBracketT):
    """A double bracket type connection.

    The reference to a connected bracket part of a
    ConnectionConfiguration. For a double bracket connection type, two
    references must be provided.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EdgeCurveRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "EdgeCurveRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_FREE_EDGE_CURVE3_D,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class EdgeReinforcementRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "EdgeReinforcementRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_EDGE_REINFORCEMENT,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class GridRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        offset:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "GridRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_REFERENCE_PLANE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class IdBaseT:
    """
    Abstract base type for all types which need to carry an ID.

    Attributes:
        custom_properties:
        id: An identifier for an element unique within the scope of the
            XML file. Each id must be unique within a document. The
            attribute uses the standard XML 1.0 ID type as defined in
            the XML Schema specification. This attribute is required in
            many OCX XML elements and an application should generate
            them automatically.
    """

    class Meta:
        name = "IdBase_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    custom_properties: Optional[CustomProperties] = field(
        default=None,
        metadata={
            "name": "CustomProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PanelRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "PanelRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PANEL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SeamRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "SeamRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_SEAM,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SingleBracket(SingleBracketT):
    """
    Double bracket connection.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SlotParameters(SlotParametersT):
    """
    Parameters of a slot (cut-out) typically used in shipbuilding.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StiffenerRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "StiffenerRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_STIFFENER,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SurfaceRefT(BoundedRefT):
    """
    Type definition.

    Attributes:
        guidref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """

    class Meta:
        name = "SurfaceRef_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_SURFACE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class DimensionSet(DimensionSetType):
    """
    Container for dimensions.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class UnitType:
    """
    Type for the unit.

    Attributes:
        unit_name:
        unit_symbol:
        root_units: Container for defining derived units in terms of
            their root units. This allows a precise definition of a wide
            range of units. The goal is to improve interoperability
            among applications and databases which use derived units
            based on commonly encountered root units.
        id:
        dimension_url: URL to a representation of the unit or quantity
            in terms of the 7 SI base dimensions.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    unit_name: list[UnitName] = field(
        default_factory=list,
        metadata={
            "name": "UnitName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "min_occurs": 1,
        },
    )
    unit_symbol: list[UnitSymbol] = field(
        default_factory=list,
        metadata={
            "name": "UnitSymbol",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        },
    )
    root_units: Optional[RootUnits] = field(
        default=None,
        metadata={
            "name": "RootUnits",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    dimension_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "dimensionURL",
            "type": "Attribute",
        },
    )


@dataclass
class CellBoundary(CellBoundaryT):
    """
    The reference to a Panel surface making up one Cell boundary.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CrossFlow(IdBaseT):
    """Concept to specify cross flow between Cells making up a Compartment.

    This enables the modelling of cells that are not adjacent but are
    connected by a piping system and part of the same Compartment.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    cell_connection: Optional[CellConnection] = field(
        default=None,
        metadata={
            "name": "CellConnection",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class DescriptionBaseT(IdBaseT):
    """
    Abstract base element for all elements that needs to carry a description.

    Attributes:
        description:
        name: An optional descriptive or display name.
    """

    class Meta:
        name = "DescriptionBase_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    description: Optional[Description] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EdgeCurveRef(EdgeCurveRefT):
    """A reference to a Panel, Plate or bracket boundary curve.

    Used as landing curve for a faceplate or edge reinforcement
    stiffener.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EdgeReinforcementRef(EdgeReinforcementRefT):
    """
    A  reference to an EdgeReinforcement.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class GridRef(GridRefT):
    """An element that makes a reference to a grid definition.

    An offset along the grid reference normal vector can be given.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class IdBase(IdBaseT):
    """
    Abstract base element for all elements which need to carry an ID.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class NamedEntityT(IdBaseT):
    """
    Abstract base element for all elements that needs to carry a mandatory name.

    Attributes:
        description:
        name: An mandatory descriptive or display name.
    """

    class Meta:
        name = "NamedEntity_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    description: Optional[Description] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PanelRef(PanelRefT):
    """
    The reference to a connected Plate.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PenetratingObjectT:
    """
    Type definition of a penetrated structural object.

    Attributes:
        plate_ref: Reference to a penetrated Plate.
        slot_parameters:
    """

    class Meta:
        name = "PenetratingObject_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    plate_ref: Optional[PlateRef] = field(
        default=None,
        metadata={
            "name": "PlateRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    slot_parameters: Optional[SlotParameters] = field(
        default=None,
        metadata={
            "name": "SlotParameters",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class SeamRef(SeamRefT):
    """
    The reference to a connected Plate.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StiffenerRef(StiffenerRefT):
    """
    A  reference to a Stiffener.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SurfaceRef(SurfaceRefT):
    """
    The reference to a Surface geometry which is shared between more than one part.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebStiffenerRef(StiffenerRefT):
    """
    Web stiffener connection.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Unit(UnitType):
    """Element for describing units.

    Use in containers UnitSet or directly incorporate into a host
    schema.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class DescriptionBase(DescriptionBaseT):
    """
    Abstract base element for all elements that need to carry a description.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EndCutT(DescriptionBaseT):
    """
    Type definition of stiffener end cut parameters.

    Attributes:
        cutback_distance:
        web_cut_back_angle:
        web_nose_height:
        flange_cut_back_angle:
        flange_nose_height:
        feature_cope:
        symmetric_flange: The end cut is symmetrical.
        sniped: The stiffener is sniped.
    """

    class Meta:
        name = "EndCut_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    cutback_distance: Optional[CutbackDistance] = field(
        default=None,
        metadata={
            "name": "CutbackDistance",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_cut_back_angle: Optional[WebCutBackAngle] = field(
        default=None,
        metadata={
            "name": "WebCutBackAngle",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_nose_height: Optional[WebNoseHeight] = field(
        default=None,
        metadata={
            "name": "WebNoseHeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    flange_cut_back_angle: Optional[FlangeCutBackAngle] = field(
        default=None,
        metadata={
            "name": "FlangeCutBackAngle",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    flange_nose_height: Optional[FlangeNoseHeight] = field(
        default=None,
        metadata={
            "name": "FlangeNoseHeight",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    feature_cope: Optional[FeatureCope] = field(
        default=None,
        metadata={
            "name": "FeatureCope",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    symmetric_flange: bool = field(
        default=False,
        metadata={
            "name": "symmetricFlange",
            "type": "Attribute",
        },
    )
    sniped: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityBaseT(DescriptionBaseT):
    """
    Abstract base for all structural parts (Panel, Plate, Seam ...)information are
    derived.

    Attributes:
        guidref: A globally Unique ID referring an entity in the sending
            application.
    """

    class Meta:
        name = "EntityBase_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class GeometryRepresentationT(DescriptionBaseT):
    """
    Type definition of the abstract base class for all structural geometry
    definitions.
    """

    class Meta:
        name = "GeometryRepresentation_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class MaterialT(NamedEntityT):
    """
    Type definition of a Material with physical properties.
    """

    class Meta:
        name = "Material_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    density: Optional[Density] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    youngs_modulus: Optional[YoungsModulus] = field(
        default=None,
        metadata={
            "name": "YoungsModulus",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    poisson_ratio: Optional[PoissonRatio] = field(
        default=None,
        metadata={
            "name": "PoissonRatio",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    yield_stress: Optional[YieldStress] = field(
        default=None,
        metadata={
            "name": "YieldStress",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    ultimate_stress: Optional[UltimateStress] = field(
        default=None,
        metadata={
            "name": "UltimateStress",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    thermal_expansion_coefficient: Optional[ThermalExpansionCoefficient] = (
        field(
            default=None,
            metadata={
                "name": "ThermalExpansionCoefficient",
                "type": "Element",
                "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            },
        )
    )
    grade: Optional[GradeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class OccurrenceT(IdBaseT):
    """
    Type Definition.

    Attributes:
        connected_bracket_ref:
        pillar_ref:
        lug_plate_ref:
        bracket_ref:
        plate_ref:
        hole_contour_ref:
        stiffener_ref:
        seam_ref:
        edge_reinforcement_ref:
        name: The name of the node
        type_value: The design/product  view type
    """

    class Meta:
        name = "Occurrence_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    connected_bracket_ref: list[ConnectedBracketRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    pillar_ref: list[PillarRef] = field(
        default_factory=list,
        metadata={
            "name": "PillarRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    lug_plate_ref: list[LugPlateRef] = field(
        default_factory=list,
        metadata={
            "name": "LugPlateRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bracket_ref: list[BracketRef] = field(
        default_factory=list,
        metadata={
            "name": "BracketRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    plate_ref: list[PlateRef] = field(
        default_factory=list,
        metadata={
            "name": "PlateRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    hole_contour_ref: list[HoleContourRef] = field(
        default_factory=list,
        metadata={
            "name": "HoleContourRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    stiffener_ref: list[StiffenerRef] = field(
        default_factory=list,
        metadata={
            "name": "StiffenerRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    seam_ref: list[SeamRef] = field(
        default_factory=list,
        metadata={
            "name": "SeamRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    edge_reinforcement_ref: list[EdgeReinforcementRef] = field(
        default_factory=list,
        metadata={
            "name": "EdgeReinforcementRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class ParametricHole2DT(DescriptionBaseT):
    """
    Type definition of a set of parametric hole definitions.
    """

    class Meta:
        name = "ParametricHole2D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ProcessLayerT(DescriptionBaseT):
    """
    Type definition for the ProcessLayer.
    """

    class Meta:
        name = "ProcessLayer_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebStiffenerWithDoubleBracketT:
    """
    Type definition of Web stiffener with double bracket connection.

    Attributes:
        connected_bracket_ref: Reference to the two connected brackets
            which are part of a ConnectionConfiguration.
        web_stiffener_ref:
    """

    class Meta:
        name = "WebStiffenerWithDoubleBracket_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    connected_bracket_ref: list[ConnectedBracketRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    web_stiffener_ref: Optional[WebStiffenerRef] = field(
        default=None,
        metadata={
            "name": "WebStiffenerRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class WebStiffenerWithSingleBracketT:
    """
    Type definition of Web stiffener with single bracket connection.
    """

    class Meta:
        name = "WebStiffenerWithSingleBracket_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    connected_bracket_ref: Optional[ConnectedBracketRef] = field(
        default=None,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    web_stiffener_ref: Optional[WebStiffenerRef] = field(
        default=None,
        metadata={
            "name": "WebStiffenerRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class WebStiffenerT:
    """
    Type definition of Web stiffener with single bracket connection.
    """

    class Meta:
        name = "WebStiffener_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    web_stiffener_ref: Optional[WebStiffenerRef] = field(
        default=None,
        metadata={
            "name": "WebStiffenerRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class UnitSetType:
    """
    Type for the unit container.

    Attributes:
        unit: Element for describing units. Use in containers UnitSet or
            directly incorporate into a host schema.
    """

    class Meta:
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    unit: list[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "min_occurs": 1,
        },
    )


@dataclass
class CellT(GeometryRepresentationT):
    """
    Type definition of the structural concept of a cell defining a part of a
    compartment (physical space).
    """

    class Meta:
        name = "Cell_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    cell_boundary: list[CellBoundary] = field(
        default_factory=list,
        metadata={
            "name": "CellBoundary",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class Curve3DT(GeometryRepresentationT):
    """
    Type definition of the abstract base class for any 3D curve.

    Attributes:
        curve_length:
        is2_d: Set to True if the Curve3D is given in 2D space.
    """

    class Meta:
        name = "Curve3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    curve_length: Optional[CurveLength] = field(
        default=None,
        metadata={
            "name": "CurveLength",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    is2_d: bool = field(
        default=False,
        metadata={
            "name": "is2D",
            "type": "Attribute",
        },
    )


@dataclass
class EndCutEnd1(EndCutT):
    """
    The stiffener end cut detailing.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EndCutEnd2(EndCutT):
    """
    Stiffener end cut detailing at end 2.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EntityBase(EntityBaseT):
    """
    Abstract base element for all structural parts (Panel, Plate, Seam ...).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EquipmentT(EntityBaseT):
    """
    Type definition of the Equipment element.
    """

    class Meta:
        name = "Equipment_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class FormT(EntityBaseT):
    """
    Abstract base type  definition of the Form element.
    """

    class Meta:
        name = "Form_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    distance_tolerance: Optional[DistanceTolerance] = field(
        default=None,
        metadata={
            "name": "DistanceTolerance",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    angle_tolerance: Optional[AngleTolerance] = field(
        default=None,
        metadata={
            "name": "AngleTolerance",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class GeometryRepresentation(GeometryRepresentationT):
    """
    Abstract base class for all structural geometry definitions.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Hole2DcontourT(GeometryRepresentationT):
    """
    Type definition of Parametric or curve based 2D contours.
    """

    class Meta:
        name = "Hole2DContour_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    hole_ref: Optional[HoleRef] = field(
        default=None,
        metadata={
            "name": "HoleRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Material(MaterialT):
    """
    Physical properties of a material.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Occurrence(OccurrenceT):
    """
    An occurrence in a DesignView is a reference to a physical part in the model.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ParametricCircleT(ParametricHole2DT):
    """
    Type definition of the  parametric circle in u-v space defined by a diameter.
    """

    class Meta:
        name = "ParametricCircle_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    diameter: Optional[Diameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ParametricHole2D(ParametricHole2DT):
    """
    A set of parametric hole definitions in u-v space.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ProcessLayer(ProcessLayerT):
    """Abstract element which can hold any process related business information.

    (To be designed).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RadialCylinderT(EntityBaseT):
    """
    Cylindrical reference system.
    """

    class Meta:
        name = "RadialCylinder_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class RectangularHoleT(ParametricHole2DT):
    """
    Type definition of  a rectangular hole with corner fillet radii.

    Attributes:
        height: The height of the hole.
        width: The width of the hole.
        fillet_radius: Corner fillet radius. If not given, the fillet
            radius is taken as 0.5*Min of (Height,Width), i.e. half of
            the smallest of the Height or the Width .
    """

    class Meta:
        name = "RectangularHole_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    fillet_radius: Optional[FilletRadius] = field(
        default=None,
        metadata={
            "name": "FilletRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class RectangularMickeyMouseEarsT(ParametricHole2DT):
    """
    A hole where the two circular parts have unequal radii.

    Attributes:
        height: The height of the hole.
        width: The width of the hole.
        radius: The radius of the Mickey Mouse ear.
        displacement:
    """

    class Meta:
        name = "RectangularMickeyMouseEars_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    displacement: Optional[Displacement] = field(
        default=None,
        metadata={
            "name": "Displacement",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class RefPlaneT(EntityBaseT):
    """
    Type definition of a reference plane used to define unbounded planar geometry.

    Attributes:
        reference_location: The location of the plane on the reference
            axis.
        display_grid:
    """

    class Meta:
        name = "RefPlane_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    reference_location: Optional[ReferenceLocation] = field(
        default=None,
        metadata={
            "name": "ReferenceLocation",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    display_grid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "displayGrid",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StructurePartT(EntityBaseT):
    """
    Type definition of  the abstract base class for structure objects representing
    structure concepts.
    """

    class Meta:
        name = "StructurePart_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    physical_properties: Optional[PhysicalProperties] = field(
        default=None,
        metadata={
            "name": "PhysicalProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class SuperEllipticalT(ParametricHole2DT):
    """Type definition of a super-elliptical hole.

    It can also describe a true ellipse.

    Attributes:
        height:
        width:
        exponent: The exponent of the super ellipse equation
            (x/Height)**e + (y/Width)**e = 1. If e=2.5 the result is a
            super ellipse while e=2.0 results in a normal ellipse.
    """

    class Meta:
        name = "SuperElliptical_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    exponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SymmetricalHoleT(ParametricHole2DT):
    """
    Type definition of a hole made of two semicircles connected by two straight
    lines.

    Attributes:
        height: The height of the hole.
        width: The width of the hole.
    """

    class Meta:
        name = "SymmetricalHole_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class WebStiffener(WebStiffenerT):
    """
    Connection configuration with one web stiffener with a single bracket
    connection.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebStiffenerWithDoubleBracket(WebStiffenerWithDoubleBracketT):
    """
    Web stiffener with double bracket connection.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class WebStiffenerWithSingleBracket(WebStiffenerWithSingleBracketT):
    """
    Connection configuration with one web stiffener with a single bracket
    connection.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UnitSet(UnitSetType):
    """Container for units.

    Use in UnitsML container or directly incorporate into a host schema.
    """

    class Meta:
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class Cell(CellT):
    """
    Structural concept of a cell defining a closed volume which is part of a
    compartment (physical space).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Circle3DT(Curve3DT):
    """
    Type definition of a circle in 3D space.

    Attributes:
        diameter: The circle diameter.
        center: The centre of the circle.
        normal: The normal vector of the    the circle plane.
    """

    class Meta:
        name = "Circle3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    diameter: Optional[Diameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    center: Optional[Center] = field(
        default=None,
        metadata={
            "name": "Center",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    normal: Optional[Normal] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class CircumArc3DT(Curve3DT):
    """
    Type definition of a 3D Line/Arc representation defined by three points in 3D
    space.
    """

    class Meta:
        name = "CircumArc3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    start_point: Optional[StartPoint] = field(
        default=None,
        metadata={
            "name": "StartPoint",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    intermediate_point: Optional[IntermediatePoint] = field(
        default=None,
        metadata={
            "name": "IntermediatePoint",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    end_point: Optional[EndPoint] = field(
        default=None,
        metadata={
            "name": "EndPoint",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class CircumCircle3DT(Curve3DT):
    """
    Type definition of a circle in 3D space defined by a circumscribed position of
    3 points.
    """

    class Meta:
        name = "CircumCircle3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    positions: Optional[Positions] = field(
        default=None,
        metadata={
            "name": "Positions",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ConnectionConfigurationT(DescriptionBaseT):
    """
    Type definition of the structural concept defining  end configurations for
    stiffeners used in shipbuilding.

    Attributes:
        single_bracket: A single bracket connection type at the position
            of the end configuration.
        double_bracket: A double bracket connection type at the position
            of the end configuration.
        web_stiffener: Web stiffener at the position of the end
            configuration.
        web_stiffener_with_single_bracket: Web stiffener with single
            bracket connection at the position of the end configuration.
        web_stiffener_with_double_bracket: A web stiffener with double
            bracket connection at the position of the end configuration.
        plate_ref: The reference to a connected Plate at this end
            configuration.
        pillar_ref: The reference to a connected Member (Pillar) at this
            end configuration.
        stiffener_ref: The reference to the connected Stiffener at this
            end configuration.
        point3_d: The logical geometric position of the end
            configuration at the stiffeners end.
    """

    class Meta:
        name = "ConnectionConfiguration_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    single_bracket: Optional[SingleBracket] = field(
        default=None,
        metadata={
            "name": "SingleBracket",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    double_bracket: Optional[DoubleBracket] = field(
        default=None,
        metadata={
            "name": "DoubleBracket",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    web_stiffener: Optional[WebStiffener] = field(
        default=None,
        metadata={
            "name": "WebStiffener",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    web_stiffener_with_single_bracket: Optional[
        WebStiffenerWithSingleBracket
    ] = field(
        default=None,
        metadata={
            "name": "WebStiffenerWithSingleBracket",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    web_stiffener_with_double_bracket: Optional[
        WebStiffenerWithDoubleBracket
    ] = field(
        default=None,
        metadata={
            "name": "WebStiffenerWithDoubleBracket",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    plate_ref: Optional[PlateRef] = field(
        default=None,
        metadata={
            "name": "PlateRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    pillar_ref: Optional[PillarRef] = field(
        default=None,
        metadata={
            "name": "PillarRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    stiffener_ref: Optional[StiffenerRef] = field(
        default=None,
        metadata={
            "name": "StiffenerRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    point3_d: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Curve3D(Curve3DT):
    """
    Abstract base class for any 3D curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Ellipse3DT(Curve3DT):
    """
    Type definition of An ellipse in 3D space.

    Attributes:
        center: The centre of the ellipse.
        major_diameter: The ellipse major diameter. It is expected that
            MajorDiameter &gt; MinorDiameter.
        minor_diameter: The diameter of the ellipse on the minor axis.
        major_axis:
        minor_axis: Definition of the ellipse minor axis direction. The
            minor axis is the cross product of the normal and the major
            axis.
        normal: The normal vector of the ellipse plane.
    """

    class Meta:
        name = "Ellipse3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    center: Optional[Center] = field(
        default=None,
        metadata={
            "name": "Center",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    major_diameter: Optional[MajorDiameter] = field(
        default=None,
        metadata={
            "name": "MajorDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    minor_diameter: Optional[MinorDiameter] = field(
        default=None,
        metadata={
            "name": "MinorDiameter",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    major_axis: Optional[MajorAxis] = field(
        default=None,
        metadata={
            "name": "MajorAxis",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    minor_axis: Optional[MinorAxis] = field(
        default=None,
        metadata={
            "name": "MinorAxis",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    normal: Optional[Normal] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Equipment(EquipmentT):
    """
    Place holder for future equipment support (To be designed).
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Form(FormT):
    """
    Abstract base class for object describing geometry and topology.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Hole2Dcontour(Hole2DcontourT):
    """
    An instantiated hole defined by a reference to a hole-shape and a
    transformation..
    """

    class Meta:
        name = "Hole2DContour"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Line3DT(Curve3DT):
    """
    Type definition of a straight line defined by two points.
    """

    class Meta:
        name = "Line3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    start_point: Optional[StartPoint] = field(
        default=None,
        metadata={
            "name": "StartPoint",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    end_point: Optional[EndPoint] = field(
        default=None,
        metadata={
            "name": "EndPoint",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class MaterialCatalogueT(DescriptionBaseT):
    """
    Type definition of the material types used and their properties recognised by
    the Society.
    """

    class Meta:
        name = "MaterialCatalogue_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    material: list[Material] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class MemberT(StructurePartT):
    """
    Abstract type definition for the Member element.
    """

    class Meta:
        name = "Member_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Nurbs3DT(Curve3DT):
    """
    Type definition of a Non-uniform rational basis spline (NURBS) curve defined by
    a set of 3D control points.
    """

    class Meta:
        name = "NURBS3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    nurbsproperties: Optional[Nurbsproperties] = field(
        default=None,
        metadata={
            "name": "NURBSproperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    knot_vector: Optional[KnotVector] = field(
        default=None,
        metadata={
            "name": "KnotVector",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    control_pt_list: Optional[ControlPtList] = field(
        default=None,
        metadata={
            "name": "ControlPtList",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class OccurrenceGroupT(IdBaseT):
    """
    Type definition.

    Attributes:
        occurrence:
        occurrence_group:
        name: The name of the node.
        type_value: The occurrence group design/product view type
    """

    class Meta:
        name = "OccurrenceGroup_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    occurrence: list[Occurrence] = field(
        default_factory=list,
        metadata={
            "name": "Occurrence",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    occurrence_group: list["OccurrenceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "OccurrenceGroup",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class ParametricCircle(ParametricCircleT):
    """
    A parametric circle in u-v space defined by a diameter.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PolyLine3DT(Curve3DT):
    """
    Type definition of a 3D curve defined by a list of 3D points composing a list
    of linear segments.

    Attributes:
        point3_d:
        is_closed: If set to true, the PolyLine3D forms a closed
            contour. The default is false.
    """

    class Meta:
        name = "PolyLine3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    point3_d: list[Point3D] = field(
        default_factory=list,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 2,
        },
    )
    is_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isClosed",
            "type": "Attribute",
        },
    )


@dataclass
class RadialCylinder(RadialCylinderT):
    """
    Cylindrical reference system.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RectangularHole(RectangularHoleT):
    """
    A rectangular hole in u-v space with corner fillets of equal radii.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RectangularMickeyMouseEars(RectangularMickeyMouseEarsT):
    """
    A rectangular hole with corner radii in the form of Mickey Mouse ears.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RefPlane(RefPlaneT):
    """
    A reference plane used to define unbounded planar geometry.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SlotContour(Hole2DcontourT):
    """
    An optional contour for the detailed slot shape given as a reference to a
    catalogue shape with a transformation.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SuperElliptical(SuperEllipticalT):
    """A super-elliptical hole.

    It can also describe a true ellipse.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SymmetricalHole(SymmetricalHoleT):
    """
    A hole made of two semicircles connected by two straight lines.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UnitsMltype:
    """
    ComplexType for the root element of an UnitsML document.
    """

    class Meta:
        name = "UnitsMLType"
        target_namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )

    unit_set: Optional[UnitSet] = field(
        default=None,
        metadata={
            "name": "UnitSet",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        },
    )
    dimension_set: Optional[DimensionSet] = field(
        default=None,
        metadata={
            "name": "DimensionSet",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        },
    )


@dataclass
class Circle3D(Circle3DT):
    """
    A circle in 3D space.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CircumArc3D(CircumArc3DT):
    """3D Line/Arc representation.

    Represents a semicircle uniquely defined by three points in 3D space
    given by the start position, intermediate position and the end
    position..
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CircumCircle3D(CircumCircle3DT):
    """
    Definition of a circle in 3D space by a circum-circle of 3 points.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ConnectionConfiguration(ConnectionConfigurationT):
    """
    The structural concept defining the end configurations for stiffeners used in
    shipbuilding.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CylindricalAxesT:
    """
    Cylindrical reference system.
    """

    class Meta:
        name = "CylindricalAxes_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    radial_cylinder: list[RadialCylinder] = field(
        default_factory=list,
        metadata={
            "name": "RadialCylinder",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class Ellipse3D(Ellipse3DT):
    """
    An ellipse in 3D space.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class EquipmentsT(EntityBaseT):
    """
    Type definition.
    """

    class Meta:
        name = "Equipments_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    equipment: list[Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class Line3D(Line3DT):
    """
    A straight line defined by two points.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class MaterialCatalogue(MaterialCatalogueT):
    """
    The material types used and their properties recognised by the Society.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Member(MemberT):
    """
    Abstract element describing structure concept parts like columns, pillars,
    beams ...
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Nurbs3D(Nurbs3DT):
    """
    Non-Uniform Rational Spline Base curve definition.
    """

    class Meta:
        name = "NURBS3D"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OccurrenceGroup(OccurrenceGroupT):
    """A grouping of occurrences.

    Can also contain other OccurrenceGroup to form a nested level of
    groups.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PenetrationT(ConnectionConfigurationT):
    """
    Type definition of Structural concept of stiffener penetration configurations
    typically used in shipbuilding.

    Attributes:
        slot_parameters:
        tightness: The tightness type of the penetration.
    """

    class Meta:
        name = "Penetration_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    slot_parameters: Optional[SlotParameters] = field(
        default=None,
        metadata={
            "name": "SlotParameters",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    tightness: Optional[TightnessValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class PhysicalSpaceT(EntityBaseT):
    """
    Type definition of the  concept of a physical compartment representing a closed
    volume (space) defined by  enclosing  structure panels.

    Attributes:
        compartment_properties:
        cell:
        cross_flow: Specify cross flow between Cells making up a
            Compartment. This enables the modelling of cells that are
            not adjacent, but are connected by a piping system and part
            of the same Compartment.
        external_geometry_ref:
        bulk_cargo:
        liquid_cargo:
        unit_cargo:
        compartment_purpose:
    """

    class Meta:
        name = "PhysicalSpace_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    compartment_properties: Optional[CompartmentProperties] = field(
        default=None,
        metadata={
            "name": "CompartmentProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    cell: list[Cell] = field(
        default_factory=list,
        metadata={
            "name": "Cell",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    cross_flow: list[CrossFlow] = field(
        default_factory=list,
        metadata={
            "name": "CrossFlow",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulk_cargo: Optional[BulkCargo] = field(
        default=None,
        metadata={
            "name": "BulkCargo",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    liquid_cargo: Optional[LiquidCargo] = field(
        default=None,
        metadata={
            "name": "LiquidCargo",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    unit_cargo: Optional[UnitCargo] = field(
        default=None,
        metadata={
            "name": "UnitCargo",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    compartment_purpose: Optional[CompartmentPurposeValue] = field(
        default=None,
        metadata={
            "name": "compartmentPurpose",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PolyLine3D(PolyLine3DT):
    """A list of 3D points defining a sequence of linear segments.

    Repeat the first position at the end of the last line segment to
    form a closed contour.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class RefPlanesT(ReferencePlaneT):
    """
    Frame table position definition.

    Attributes:
        ref_plane:
        is_main_system: True if this is the main reference system
            definition.
    """

    class Meta:
        name = "RefPlanes_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    ref_plane: list[RefPlane] = field(
        default_factory=list,
        metadata={
            "name": "RefPlane",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    is_main_system: bool = field(
        default=True,
        metadata={
            "name": "isMainSystem",
            "type": "Attribute",
        },
    )


@dataclass
class UnitsMl(UnitsMltype):
    """
    Container for UnitsML units, quantities, and prefixes.
    """

    class Meta:
        name = "UnitsML"
        namespace = (
            "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
        )


@dataclass
class CompositeCurve3DT(Curve3DT):
    """
    Type definition of a composite curve composed of a collection of Line3D,
    CircumArc3D and/or NURBS segments..
    """

    class Meta:
        name = "CompositeCurve3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    poly_line3_d: list[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    line3_d: list[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbs3_d: list[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circum_arc3_d: list[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class CylindricalAxes(CylindricalAxesT):
    """
    Cylindrical reference system.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class DesignViewT(DescriptionBaseT):
    """
    Type definition.
    """

    class Meta:
        name = "DesignView_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    vessel_ref: Optional[VesselRef] = field(
        default=None,
        metadata={
            "name": "VesselRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    occurrence_group: list[OccurrenceGroup] = field(
        default_factory=list,
        metadata={
            "name": "OccurrenceGroup",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    occurrence: list[Occurrence] = field(
        default_factory=list,
        metadata={
            "name": "Occurrence",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Equipments(EquipmentsT):
    """
    Container for equipments.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Penetration(PenetrationT):
    """
    Structural concept of stiffener penetration configurations typically used in
    shipbuilding.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PhysicalSpace(PhysicalSpaceT):
    """
    The concept of a physical compartment representing a closed volume (space)
    defined by  enclosing  structure panels.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class XrefPlanes(RefPlanesT):
    """A collection of Y-Z planes used as object limits.

    Can also be used to create a frame table definition for display
    purposes. The exporting application will then have to provide all
    grid positions.

    Attributes:
        distance_to_ap:
        is_reversed: For most vessels the X reference positions are
            given aft to forward which is the default. Set
            isReversed=true if  the frame positions are given from fore
            to aft  (normally this is the case for naval vessels).
    """

    class Meta:
        name = "XRefPlanes"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    distance_to_ap: Optional[DistanceToAp] = field(
        default=None,
        metadata={
            "name": "DistanceToAP",
            "type": "Element",
        },
    )
    is_reversed: bool = field(
        default=False,
        metadata={
            "name": "isReversed",
            "type": "Attribute",
        },
    )


@dataclass
class YrefPlanes(RefPlanesT):
    """A collection of X-Z planes used as object limits.

    Can also be used to create a frame table definition for display
    purposes. The exporting application will then have to provide all
    grid positions.
    """

    class Meta:
        name = "YRefPlanes"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ZrefPlanes(RefPlanesT):
    """A collection of X-Y planes used as object limits.

    Can also be used to create a frame table definition for display
    purposes. The exporting application will then have to provide all
    grid positions.
    """

    class Meta:
        name = "ZRefPlanes"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CompositeCurve3D(CompositeCurve3DT):
    """The concept of a composite curve composed of a collection of Line3D,
    CircumArc3D and/or NURBS segments.

    Curves are sorted end to end and have C0 continuity across each
    segment in the CompositeCurve3D definition.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CoordinateSystemT(EntityBaseT):
    """
    Type definition of the vessel coordinate system A right-handed orthogonal
    Cartesian coordinate system.

    Attributes:
        xref_planes:
        yref_planes:
        zref_planes:
        local_cartesian:
        is_global: If set to true, the coordinate system is the global
            world coordinate frame with right-handed convention. This is
            the default.
    """

    class Meta:
        name = "CoordinateSystem_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    xref_planes: Optional[XrefPlanes] = field(
        default=None,
        metadata={
            "name": "XRefPlanes",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    yref_planes: Optional[YrefPlanes] = field(
        default=None,
        metadata={
            "name": "YRefPlanes",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    zref_planes: Optional[ZrefPlanes] = field(
        default=None,
        metadata={
            "name": "ZRefPlanes",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    local_cartesian: Optional[LocalCartesian] = field(
        default=None,
        metadata={
            "name": "LocalCartesian",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    is_global: bool = field(
        default=True,
        metadata={
            "name": "isGlobal",
            "type": "Attribute",
        },
    )


@dataclass
class DesignView(DesignViewT):
    """
    A manifestation of some or all the components in the exporting application that
    contains configuration information for the parts it includes.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SweepCurve(CompositeCurve3DT):
    """
    The sweep direction and extent is defined by a general 3D sweep curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BaseCurveT(Curve3DT):
    class Meta:
        name = "BaseCurve_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    circum_arc3_d: list[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbs3_d: list[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    composite_curve3_d: list[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    line3_d: list[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    poly_line3_d: list[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circum_circle3_d: list[CircumCircle3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ellipse3_d: list[Ellipse3D] = field(
        default_factory=list,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circle3_d: list[Circle3D] = field(
        default_factory=list,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Contour3DT:
    """The geometry of a closed contour limiting a surface, represented by a set of
    trim curves or a closed curve primitive.

    The contour curve must form a closed curve.
    """

    class Meta:
        name = "Contour3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    circum_arc3_d: list[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbs3_d: list[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    composite_curve3_d: list[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    line3_d: list[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    poly_line3_d: list[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circum_circle3_d: list[CircumCircle3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ellipse3_d: list[Ellipse3D] = field(
        default_factory=list,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circle3_d: list[Circle3D] = field(
        default_factory=list,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class CoordinateSystem(CoordinateSystemT):
    """A right-handed orthogonal Cartesian coordinate system.

    Used to define the vessel coordinate system definition., either in
    world coordinates (mandatory) or as additional local systems if
    necessary.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FreeEdgeCurve3DT(Curve3DT):
    """
    The type definition of a free edge defined by a collection of non-closed
    Curve3D types.

    Attributes:
        circum_arc3_d:
        nurbs3_d:
        composite_curve3_d:
        line3_d:
        poly_line3_d:
        circum_circle3_d:
        ellipse3_d:
        circle3_d:
        is_uvspace: Default is "false". Set this attribute to true if
            the FreeEdgeCurve is represented by coordinates in the UV
            space. This should only be used when a FreeEdgeCurve is used
            to trim NURBS surface patches where the trim curve is only
            used to trim the underlying surface. When the curve is given
            in UV space, the X,Y point coordinates are replaced with the
            U,V coordinates. In this case the Z coordinate should be set
            to zero. The Z coordinate will not be used by the importing
            application.
    """

    class Meta:
        name = "FreeEdgeCurve3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    circum_arc3_d: list[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbs3_d: list[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    composite_curve3_d: list[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    line3_d: list[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    poly_line3_d: list[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circum_circle3_d: list[CircumCircle3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ellipse3_d: list[Ellipse3D] = field(
        default_factory=list,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    circle3_d: list[Circle3D] = field(
        default_factory=list,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    is_uvspace: bool = field(
        default=False,
        metadata={
            "name": "isUVSpace",
            "type": "Attribute",
        },
    )


@dataclass
class TraceLineT:
    """
    The type definition of the stiffener TraceLine.
    """

    class Meta:
        name = "TraceLine_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    composite_curve3_d: Optional[CompositeCurve3D] = field(
        default=None,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class BaseCurve(BaseCurveT):
    """
    The base curve defining an extruded surface when it is swept.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Contour(Contour3DT):
    """
    The contour of a surface or structure part.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class FaceBoundaryCurve(Contour3DT):
    """
    A collection of 3D curves making up a closed boundary.

    Attributes:
        is_uvspace: If set to True, the FacBoundaryCurve is defined in
            the parametric UV space. The Pont3D X and Y corresponds to U
            and V while the Z coordinate is disregarded. The default is
            False, i.e. the FaceBoundaryCurve is defined in the 3D
            space.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    is_uvspace: bool = field(
        default=False,
        metadata={
            "name": "isUVspace",
            "type": "Attribute",
        },
    )


@dataclass
class FreeEdgeCurve3D(FreeEdgeCurve3DT):
    """
    A single Curve3D or a collection of continuous non-closed Curve3D types which
    are used to represent a free edge of a panel or plate in shipbuilding.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class InnerContour(Contour3DT):
    """
    Any closed contour of an inner opening in a plate.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OuterContour(Contour3DT):
    """
    The geometry of the outer closed contour limiting a surface, represented by a
    set of trim curves or a closed curve primitive.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SectionInnerShape(Contour3DT):
    """
    Optional arbitrary inner section shape for hollow sections.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SectionOuterShape(Contour3DT):
    """An optional arbitrary contour  representing the outer section shape.

    Used to display the section by extrusion of the section shape along
    the trace line.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class TraceLine(TraceLineT):
    """
    The landing curve on the moulded panel surface represented by any Curve3D type.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CutByT:
    """
    Type definition of  a structural concept defining a cut-out in a surface
    defined by a parametric hole or a set of generic trim curves.
    """

    class Meta:
        name = "CutBy_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    hole2_dcontour: list[Hole2Dcontour] = field(
        default_factory=list,
        metadata={
            "name": "Hole2DContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    inner_contour: list[InnerContour] = field(
        default_factory=list,
        metadata={
            "name": "InnerContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class EdgeReinforcementT(StructurePartT):
    class Meta:
        name = "EdgeReinforcement_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    material_ref: Optional[MaterialRef] = field(
        default=None,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    inclination: list[Inclination] = field(
        default_factory=list,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    edge_curve_ref: list[EdgeCurveRef] = field(
        default_factory=list,
        metadata={
            "name": "EdgeCurveRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    hole_contour_ref: list[HoleContourRef] = field(
        default_factory=list,
        metadata={
            "name": "HoleContourRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    grid_ref: list[GridRef] = field(
        default_factory=list,
        metadata={
            "name": "GridRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    trace_line: list[TraceLine] = field(
        default_factory=list,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Hole2DT(NamedEntityT):
    """
    Type definition for a 2D hole shape defined either by a choice of a parametric
    hole or a contour curve.
    """

    class Meta:
        name = "Hole2D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    rectangular_hole: Optional[RectangularHole] = field(
        default=None,
        metadata={
            "name": "RectangularHole",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    super_elliptical: Optional[SuperElliptical] = field(
        default=None,
        metadata={
            "name": "SuperElliptical",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    symmetrical_hole: Optional[SymmetricalHole] = field(
        default=None,
        metadata={
            "name": "SymmetricalHole",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    parametric_circle: Optional[ParametricCircle] = field(
        default=None,
        metadata={
            "name": "ParametricCircle",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    contour: Optional[Contour] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class LimitedByT:
    """
    Type definition of the LimitedBy (reference to limiting objects forming a
    closed contour of the parent element).

    Attributes:
        free_edge_curve3_d: Collection of non-closed Curve3D types. Used
            to represent a free edge to form a closed contour together
            with the limiting objects.
        edge_reinforcement_ref:
        stiffener_ref:
        panel_ref:
        seam_ref:
        surface_ref:
        edge_curve_ref:
        grid_ref:
    """

    class Meta:
        name = "LimitedBy_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    free_edge_curve3_d: list[FreeEdgeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "FreeEdgeCurve3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    edge_reinforcement_ref: list[EdgeReinforcementRef] = field(
        default_factory=list,
        metadata={
            "name": "EdgeReinforcementRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    stiffener_ref: list[StiffenerRef] = field(
        default_factory=list,
        metadata={
            "name": "StiffenerRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    panel_ref: list[PanelRef] = field(
        default_factory=list,
        metadata={
            "name": "PanelRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    seam_ref: list[SeamRef] = field(
        default_factory=list,
        metadata={
            "name": "SeamRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    surface_ref: list[SurfaceRef] = field(
        default_factory=list,
        metadata={
            "name": "SurfaceRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    edge_curve_ref: list[EdgeCurveRef] = field(
        default_factory=list,
        metadata={
            "name": "EdgeCurveRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    grid_ref: list[GridRef] = field(
        default_factory=list,
        metadata={
            "name": "GridRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class PlateCutByT:
    """
    Type definition.
    """

    class Meta:
        name = "PlateCutBy_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    hole2_dcontour: list[Hole2Dcontour] = field(
        default_factory=list,
        metadata={
            "name": "Hole2DContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    outer_contour: list[OuterContour] = field(
        default_factory=list,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    slot_contour: list[SlotContour] = field(
        default_factory=list,
        metadata={
            "name": "SlotContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class SeamT(EntityBaseT):
    """
    Type definition of the Seam element describing plate seams.
    """

    class Meta:
        name = "Seam_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class SurfaceT(GeometryRepresentationT):
    """
    Type definition of the  Abstract base class for surface definitions.

    Attributes:
        face_boundary_curve: A collection of 3D curves making up a
            closed boundary. To be used whenever the surface need to be
            bounded.
    """

    class Meta:
        name = "Surface_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    face_boundary_curve: Optional[FaceBoundaryCurve] = field(
        default=None,
        metadata={
            "name": "FaceBoundaryCurve",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class UserDefinedBarSectionT:
    """
    Attributes:
        section_properties:
        section_outer_shape:
        section_inner_shape:
        custom_properties:
        number_of_parameters: Number of additional user-defined
            properties included in the definition.
    """

    class Meta:
        name = "UserDefinedBarSection_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    section_properties: Optional[SectionProperties] = field(
        default=None,
        metadata={
            "name": "SectionProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    section_outer_shape: Optional[SectionOuterShape] = field(
        default=None,
        metadata={
            "name": "SectionOuterShape",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    section_inner_shape: Optional[SectionInnerShape] = field(
        default=None,
        metadata={
            "name": "SectionInnerShape",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    custom_properties: Optional[CustomProperties] = field(
        default=None,
        metadata={
            "name": "CustomProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    number_of_parameters: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfParameters",
            "type": "Attribute",
        },
    )


@dataclass
class Cone3DT(SurfaceT):
    """
    Type definition of the Cone surface defined by origin, radius and position of
    the cone tip.

    Attributes:
        origin: The origin or centre of the cone at the base.
        tip:
        base_radius:
        tip_radius: Cone tip radius (default = 0).
    """

    class Meta:
        name = "Cone3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    tip: Optional[Tip] = field(
        default=None,
        metadata={
            "name": "Tip",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    base_radius: Optional[BaseRadius] = field(
        default=None,
        metadata={
            "name": "BaseRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    tip_radius: Optional[TipRadius] = field(
        default=None,
        metadata={
            "name": "TipRadius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class CutBy(CutByT):
    """
    A structural concept defining a cut-out in a surface defined by a parametric
    hole or a set of generic trim curves.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Cylinder3DT(SurfaceT):
    """
    Type definition of the cylindrical surface defined by root point, axis
    direction, radius and height.

    Attributes:
        origin: Cylinder anchor position.
        axis:
        radius: Cylinder radius.
        height: Cylinder height relative to origin.
    """

    class Meta:
        name = "Cylinder3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    axis: Optional[Axis] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class EdgeReinforcement(EdgeReinforcementT):
    """An EdgeReinforcement is used as a faceplate or edge reinforcement for a
    Panel, Plate or Bracket.

    The EdgeReinforcement is composed of a BarSection (usually a flat
    bar profile) and is attached to a FreeEdgeCurve which is part of the
    Panel or Plate LimitedBy. The EdgeReinforcement can reference one or
    more limits for the Panel/Plate/Bracket. At the same time the
    EdgeReinforcement provides its own TraceLine to determine the actual
    extent of the reinforcement.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ExtrudedSurfaceT(SurfaceT):
    """
    Type definition of an extruded surface defined by a base curve and a sweep path
    with extent.

    Attributes:
        base_curve: The base curve which is extruded, defining an
            extruded surface when it is swept.
        sweep:
        sweep_curve:
    """

    class Meta:
        name = "ExtrudedSurface_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    base_curve: Optional[BaseCurve] = field(
        default=None,
        metadata={
            "name": "BaseCurve",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    sweep: Optional[Sweep] = field(
        default=None,
        metadata={
            "name": "Sweep",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    sweep_curve: Optional[SweepCurve] = field(
        default=None,
        metadata={
            "name": "SweepCurve",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Hole2D(Hole2DT):
    """
    A 2D hole shape defined either by a parametric hole or a curve contour.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class LimitedBy(LimitedByT):
    """The references to limiting objects forming a closed contour of the parent
    element.

    It is not required that the set of objects is ordered in the correct
    sequence.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class NurbssurfaceT(SurfaceT):
    """
    Type definition of a Non-uniform rational basis surface definition defined by a
    grid of 3D control points.

    Attributes:
        u_nurbsproperties: Properties of the basis function in V
            direction.
        uknot_vector:
        v_nurbsproperties: Properties of the basis function in V
            direction.
        vknot_vector:
        control_pt_list:
    """

    class Meta:
        name = "NURBSSurface_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    u_nurbsproperties: Optional[UNurbsproperties] = field(
        default=None,
        metadata={
            "name": "U_NURBSproperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    uknot_vector: Optional[UknotVector] = field(
        default=None,
        metadata={
            "name": "UknotVector",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    v_nurbsproperties: Optional[VNurbsproperties] = field(
        default=None,
        metadata={
            "name": "V_NURBSproperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    vknot_vector: Optional[VknotVector] = field(
        default=None,
        metadata={
            "name": "VknotVector",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    control_pt_list: list[ControlPtList] = field(
        default_factory=list,
        metadata={
            "name": "ControlPtList",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class PlateCutBy(PlateCutByT):
    """
    A structural concept defining a cut-out in a surface defined by a parametric
    hole or a set of generic trim curves.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Seam(SeamT):
    """
    Element describing the structure concept of a plate seam.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Sphere3DT(SurfaceT):
    """
    Type definition of a Spherical surface defined by origin and radius.

    Attributes:
        origin: The origin or centre of the sphere.
        radius: The radius of the sphere.
    """

    class Meta:
        name = "Sphere3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Surface(SurfaceT):
    """
    Abstract base class for surface definitions.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UserDefinedBarSection(UserDefinedBarSectionT):
    """
    User defined or unknown bar type.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BarSectionT(DescriptionBaseT):
    """
    Type definition of the  catalogue of rolled and welded cross-sections
    recognised by the Society.

    Attributes:
        rectangular_tube:
        octagon_bar:
        square_bar:
        bulb_flat:
        flat_bar:
        ubar:
        ibar:
        lbar_of:
        zbar:
        round_bar:
        lbar:
        tbar:
        lbar_ow:
        half_round_bar:
        hexagon_bar:
        tube:
        user_defined_bar_section:
        type_code: Section type code from manufacturer.
        short_id: Section  short id.
        manufacture:
        guidref:
    """

    class Meta:
        name = "BarSection_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    rectangular_tube: Optional[RectangularTube] = field(
        default=None,
        metadata={
            "name": "RectangularTube",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    octagon_bar: Optional[OctagonBar] = field(
        default=None,
        metadata={
            "name": "OctagonBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    square_bar: Optional[SquareBar] = field(
        default=None,
        metadata={
            "name": "SquareBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulb_flat: Optional[BulbFlat] = field(
        default=None,
        metadata={
            "name": "BulbFlat",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    flat_bar: Optional[FlatBar] = field(
        default=None,
        metadata={
            "name": "FlatBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ubar: Optional[Ubar] = field(
        default=None,
        metadata={
            "name": "UBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ibar: Optional[Ibar] = field(
        default=None,
        metadata={
            "name": "IBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    lbar_of: Optional[LbarOf] = field(
        default=None,
        metadata={
            "name": "LBarOF",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    zbar: Optional[Zbar] = field(
        default=None,
        metadata={
            "name": "ZBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    round_bar: Optional[RoundBar] = field(
        default=None,
        metadata={
            "name": "RoundBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    lbar: Optional[Lbar] = field(
        default=None,
        metadata={
            "name": "LBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    tbar: Optional[Tbar] = field(
        default=None,
        metadata={
            "name": "TBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    lbar_ow: Optional[LbarOw] = field(
        default=None,
        metadata={
            "name": "LBarOW",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    half_round_bar: Optional[HalfRoundBar] = field(
        default=None,
        metadata={
            "name": "HalfRoundBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    hexagon_bar: Optional[HexagonBar] = field(
        default=None,
        metadata={
            "name": "HexagonBar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    tube: Optional[Tube] = field(
        default=None,
        metadata={
            "name": "Tube",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    user_defined_bar_section: Optional[UserDefinedBarSection] = field(
        default=None,
        metadata={
            "name": "UserDefinedBarSection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
    short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortID",
            "type": "Attribute",
        },
    )
    manufacture: Optional[ManufactureValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class Cone3D(Cone3DT):
    """
    Definition of the Cone surface defined by origin, radius and position of the
    cone tip.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Cylinder3D(Cylinder3DT):
    """
    Definition of the cylindrical surface defined by root point, axis direction,
    radius and height.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ExtrudedSurface(ExtrudedSurfaceT):
    """
    Definition of an extruded surface defined by a base curve and either a sweep
    direction and length or a sweep curve.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HoleShapeCatalogueT(DescriptionBaseT):
    """
    Type definition of the geometry used to describe the shape of a hole.

    Attributes:
        hole2_d: 2D hole definition based on either a geometric or
            parametric definition.
    """

    class Meta:
        name = "HoleShapeCatalogue_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    hole2_d: list[Hole2D] = field(
        default_factory=list,
        metadata={
            "name": "Hole2D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class Nurbssurface(NurbssurfaceT):
    """
    Non-uniform rational basis surface definition defined by a net (grid) of
    polynomial basis functions  in U and V direction.
    """

    class Meta:
        name = "NURBSSurface"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class PillarT(MemberT):
    """
    Type definition of the structural concept for pillars used as vertical support
    in ship building.

    Attributes:
        material_ref:
        section_ref:
        trace_line: The pillar trace-line represented by a Curve3D type.
        inclination:
        limited_by:
        cut_by:
        penetration:
        connection_configuration: The connection configuration at end 1
            and/or end 2 of the pillar.
        function_type:
    """

    class Meta:
        name = "Pillar_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    material_ref: Optional[MaterialRef] = field(
        default=None,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    inclination: list[Inclination] = field(
        default_factory=list,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    penetration: list[Penetration] = field(
        default_factory=list,
        metadata={
            "name": "Penetration",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    connection_configuration: list[ConnectionConfiguration] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionConfiguration",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "max_occurs": 2,
        },
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Plane3DT(SurfaceT):
    """
    Type definition of a  Planar surface defined by Root Point and Normal.

    Attributes:
        origin: A point on the plane.
        normal: The planes normal.
        udirection: Optional local U direction of the plane.
        limited_by:
    """

    class Meta:
        name = "Plane3D_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    normal: Optional[Normal] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    udirection: Optional[Udirection] = field(
        default=None,
        metadata={
            "name": "UDirection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Sphere3D(Sphere3DT):
    """
    Definition of a Spherical surface defined by origin and radius.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SplitByT:
    """
    Type definition of Structural concepts defining the subdivision of a panel into
    plates split by one or more seams.
    """

    class Meta:
        name = "SplitBy_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    seam: list[Seam] = field(
        default_factory=list,
        metadata={
            "name": "Seam",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class StiffenerT(StructurePartT):
    """
    Type definition of the Stiffener structure concept.

    Attributes:
        trace_line:
        material_ref:
        section_ref:
        inclination:
        end_cut_end1: The stiffener end cut detailing at end 1.
        end_cut_end2: The stiffener end cut detailing at end 2.
        offset:
        connection_configuration: The stiffener end configuration at end
            1 and/or end 2 of the parent stiffener.
        penetration: A structural concept of stiffener penetration
            configurations typically used in shipbuilding.
        cut_by:
        limited_by: The references to limiting objects forming a closed
            contour of the parent element.
        function_type:
    """

    class Meta:
        name = "Stiffener_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    material_ref: Optional[MaterialRef] = field(
        default=None,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    inclination: list[Inclination] = field(
        default_factory=list,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    end_cut_end1: Optional[EndCutEnd1] = field(
        default=None,
        metadata={
            "name": "EndCutEnd1",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    end_cut_end2: Optional[EndCutEnd2] = field(
        default=None,
        metadata={
            "name": "EndCutEnd2",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    connection_configuration: list[ConnectionConfiguration] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionConfiguration",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "max_occurs": 2,
        },
    )
    penetration: list[Penetration] = field(
        default_factory=list,
        metadata={
            "name": "Penetration",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class BarSection(BarSectionT):
    """
    A catalogue of rolled and welded cross-sections recognised by the Society.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class HoleShapeCatalogue(HoleShapeCatalogueT):
    """
    Catalogue of 2D hole shapes.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Pillar(PillarT):
    """
    Structural concept for pillars used as vertical support in ship building.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Plane3D(Plane3DT):
    """
    Definition of a  Planar surface defined by Root Point and Normal.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SplitBy(SplitByT):
    """
    Structural concepts defining the subdivision of a panel into plates split by
    one or more seams.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Stiffener(StiffenerT):
    """
    Element describing the structure concept of type stiffeners which are attached
    to plating and constitutes the scantlings.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class StiffenedByT:
    """
    Type definition of the structural concept defining the stiffeners which belongs
    to a panel as a choice of a Stiffener or EdgeReinforcement.
    """

    class Meta:
        name = "StiffenedBy_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    stiffener: list[Stiffener] = field(
        default_factory=list,
        metadata={
            "name": "Stiffener",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    edge_reinforcement: list[EdgeReinforcement] = field(
        default_factory=list,
        metadata={
            "name": "EdgeReinforcement",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class SurfaceCollectionT(DescriptionBaseT):
    class Meta:
        name = "SurfaceCollection_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    plane3_d: list[Plane3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbssurface: list[Nurbssurface] = field(
        default_factory=list,
        metadata={
            "name": "NURBSSurface",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    extruded_surface: list[ExtrudedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ExtrudedSurface",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    sphere3_d: list[Sphere3D] = field(
        default_factory=list,
        metadata={
            "name": "Sphere3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cone3_d: list[Cone3D] = field(
        default_factory=list,
        metadata={
            "name": "Cone3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cylinder3_d: list[Cylinder3D] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_length": 1,
            "max_length": 40,
        },
    )


@dataclass
class UnboundedGeometryT:
    """
    Type definition of an unbounded surface geometry of the parent element.
    """

    class Meta:
        name = "UnboundedGeometry_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    plane3_d: list[Plane3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbssurface: list[Nurbssurface] = field(
        default_factory=list,
        metadata={
            "name": "NURBSSurface",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    extruded_surface: list[ExtrudedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ExtrudedSurface",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    sphere3_d: list[Sphere3D] = field(
        default_factory=list,
        metadata={
            "name": "Sphere3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cone3_d: list[Cone3D] = field(
        default_factory=list,
        metadata={
            "name": "Cone3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cylinder3_d: list[Cylinder3D] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    grid_ref: list[GridRef] = field(
        default_factory=list,
        metadata={
            "name": "GridRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    surface_ref: list[SurfaceRef] = field(
        default_factory=list,
        metadata={
            "name": "SurfaceRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class XsectionCatalogueT(NamedEntityT):
    """
    Type definition of the cross-section types for stiffeners and their properties
    recognised by the Society.
    """

    class Meta:
        name = "XSectionCatalogue_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    bar_section: list[BarSection] = field(
        default_factory=list,
        metadata={
            "name": "BarSection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )


@dataclass
class StiffenedBy(StiffenedByT):
    """
    Structural concept defining the stiffeners which belongs to a panel.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class SurfaceCollection(SurfaceCollectionT):
    """A collection of any number of surfaces.

    The surfaces have to be connected (no dis-joint surfaces). Most
    typically the SurfaceCollection will include the outer shell
    geometry definition of the vessel.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class UnboundedGeometry(UnboundedGeometryT):
    """
    The unbounded surface geometry of the parent element.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class XsectionCatalogue(XsectionCatalogueT):
    """
    The cross-section types for stiffeners and their properties recognised by the
    Society.
    """

    class Meta:
        name = "XSectionCatalogue"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class BracketT(StructurePartT):
    """
    Type definition  of Structural concept of brackets used in shipbuilding.
    """

    class Meta:
        name = "Bracket_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    bracket_parameters: Optional[BracketParameters] = field(
        default=None,
        metadata={
            "name": "BracketParameters",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    plate_material: Optional[PlateMaterial] = field(
        default=None,
        metadata={
            "name": "PlateMaterial",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    outer_contour: Optional[OuterContour] = field(
        default=None,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    unbounded_geometry: Optional[UnboundedGeometry] = field(
        default=None,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    inner_contour: list[InnerContour] = field(
        default_factory=list,
        metadata={
            "name": "InnerContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    stiffened_by: Optional[StiffenedBy] = field(
        default=None,
        metadata={
            "name": "StiffenedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class ClassCatalogueT(DescriptionBaseT):
    """
    Type definition of the Class catalogues provided as part of the OCX.

    Attributes:
        material_catalogue: Catalogue of material types and their
            properties.
        xsection_catalogue: Catalogue of section types and their
            properties.
        hole_shape_catalogue: Catalogue of 2D hole shapes.
    """

    class Meta:
        name = "ClassCatalogue_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    material_catalogue: Optional[MaterialCatalogue] = field(
        default=None,
        metadata={
            "name": "MaterialCatalogue",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    xsection_catalogue: Optional[XsectionCatalogue] = field(
        default=None,
        metadata={
            "name": "XSectionCatalogue",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    hole_shape_catalogue: Optional[HoleShapeCatalogue] = field(
        default=None,
        metadata={
            "name": "HoleShapeCatalogue",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class CompartmentFaceT(EntityBaseT):
    """
    Type definition of the face of a compartment defined by a surface boundary.

    Attributes:
        unbounded_geometry:
        face_boundary_curve: A collection of 3D curves making up the
            closed boundary of the compartment face.
    """

    class Meta:
        name = "CompartmentFace_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    unbounded_geometry: Optional[UnboundedGeometry] = field(
        default=None,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    face_boundary_curve: Optional[FaceBoundaryCurve] = field(
        default=None,
        metadata={
            "name": "FaceBoundaryCurve",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class PlateT(StructurePartT):
    """
    Type definition of Structural concept of  plates used in shipbuilding.

    Attributes:
        net_area:
        outer_contour:
        plate_material:
        limited_by:
        offset: The material offset form the parent surface. A material
            offset is measured positive along the parent surface normal
            vector.
        unbounded_geometry:
        plate_cut_by: A structural concept defining a cut-out in a
            surface defined by a parametric hole or a set of generic
            trim curves. Cut-outs on plate will only remove material of
            the parent plate, no other parts. Apply cutBy either on
            Panel or on Plate level, but not on both.
        function_type:
    """

    class Meta:
        name = "Plate_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    net_area: Optional[NetArea] = field(
        default=None,
        metadata={
            "name": "NetArea",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    outer_contour: Optional[OuterContour] = field(
        default=None,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    plate_material: Optional[PlateMaterial] = field(
        default=None,
        metadata={
            "name": "PlateMaterial",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    unbounded_geometry: Optional[UnboundedGeometry] = field(
        default=None,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    plate_cut_by: Optional[PlateCutBy] = field(
        default=None,
        metadata={
            "name": "PlateCutBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class ReferenceSurfacesT:
    """
    Type definition of a collection of surfaces.
    """

    class Meta:
        name = "ReferenceSurfaces_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    plane3_d: list[Plane3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    nurbssurface: list[Nurbssurface] = field(
        default_factory=list,
        metadata={
            "name": "NURBSSurface",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    extruded_surface: list[ExtrudedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ExtrudedSurface",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    sphere3_d: list[Sphere3D] = field(
        default_factory=list,
        metadata={
            "name": "Sphere3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cone3_d: list[Cone3D] = field(
        default_factory=list,
        metadata={
            "name": "Cone3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cylinder3_d: list[Cylinder3D] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder3D",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    surface_collection: list[SurfaceCollection] = field(
        default_factory=list,
        metadata={
            "name": "SurfaceCollection",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Bracket(BracketT):
    """
    Structural concept of brackets used in shipbuilding.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ClassCatalogue(ClassCatalogueT):
    """The Class catalogues provided as part of the OCX.

    The catalogue can hold the societys definitions of cross-sections,
    materials, hole shapes etc.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CompartmentFace(CompartmentFaceT):
    """
    The face of a compartment defined by a surface boundary.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Plate(PlateT):
    """
    Structural concept of plates used in shipbuilding.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ReferenceSurfaces(ReferenceSurfacesT):
    """
    Collection of frequently used surfaces which are referenced by more than one
    object.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class CompartmentT(EntityBaseT):
    """
    Type definition of the  concept of a compartment part of the vessel capacity
    plan representing a closed volume (space) defined by  enclosing  structure
    panels.

    Attributes:
        compartment_properties:
        compartment_face: The face of a compartment defined by a surface
            boundary. All faces must make up a CLOSED volume defining
            the compartment.
        external_geometry_ref:
        bulk_cargo:
        liquid_cargo:
        unit_cargo:
        compartment_purpose:
    """

    class Meta:
        name = "Compartment_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    compartment_properties: Optional[CompartmentProperties] = field(
        default=None,
        metadata={
            "name": "CompartmentProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    compartment_face: list[CompartmentFace] = field(
        default_factory=list,
        metadata={
            "name": "CompartmentFace",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bulk_cargo: Optional[BulkCargo] = field(
        default=None,
        metadata={
            "name": "BulkCargo",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    liquid_cargo: Optional[LiquidCargo] = field(
        default=None,
        metadata={
            "name": "LiquidCargo",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    unit_cargo: Optional[UnitCargo] = field(
        default=None,
        metadata={
            "name": "UnitCargo",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    compartment_purpose: Optional[CompartmentPurposeValue] = field(
        default=None,
        metadata={
            "name": "compartmentPurpose",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class ComposedOfT:
    class Meta:
        name = "ComposedOf_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    plate: list[Plate] = field(
        default_factory=list,
        metadata={
            "name": "Plate",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    bracket: list[Bracket] = field(
        default_factory=list,
        metadata={
            "name": "Bracket",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    pillar: list[Pillar] = field(
        default_factory=list,
        metadata={
            "name": "Pillar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Compartment(CompartmentT):
    """
    The concept of a compartment part of the vessel capacity plan representing a
    closed volume (space) defined by enclosing surface geometry.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ComposedOf(ComposedOfT):
    """
    Element representing the structural concepts which composes a structure Panel.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class ArrangementT(DescriptionBaseT):
    """
    Type definition of the vessel arrangement (of compartments).

    Attributes:
        compartment: The  concept of a compartment part of the vessel
            arrangement  representing a CLOSED volume (space) defined by
            enclosing surface geometry.
        physical_space:
    """

    class Meta:
        name = "Arrangement_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    compartment: list[Compartment] = field(
        default_factory=list,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    physical_space: list[PhysicalSpace] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalSpace",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class PanelT(EntityBaseT):
    """Type definition of Structural concept of shipbuilding panels.

    Panels can typically be composed of plates, seams and stiffeners.

    Attributes:
        unbounded_geometry: The unbounded surface geometry of the parent
            element. Can be a patch of connected surfaces.
        limited_by:
        composed_of: The element representing the structural concepts
            which composes the structural Panel. If no ComposedOf
            definition is given, the Panel is treated as a virtual
            panel. A virtual panel is used to limit other objects
            defining the model topology.
        physical_properties:
        outer_contour:
        stiffened_by:
        split_by:
        cut_by: A structural concept defining a cut-out in a surface
            defined by a parametric hole or a set of generic trim
            curves. Cut-out on panels will cut material on all the panel
            plates touched by the cut-out shape. Apply cutBy either on
            Panel or on Plate level, but not on both.
        function_type:
        tightness:
    """

    class Meta:
        name = "Panel_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    unbounded_geometry: Optional[UnboundedGeometry] = field(
        default=None,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    composed_of: Optional[ComposedOf] = field(
        default=None,
        metadata={
            "name": "ComposedOf",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    physical_properties: Optional[PhysicalProperties] = field(
        default=None,
        metadata={
            "name": "PhysicalProperties",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    outer_contour: Optional[OuterContour] = field(
        default=None,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    stiffened_by: Optional[StiffenedBy] = field(
        default=None,
        metadata={
            "name": "StiffenedBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    split_by: Optional[SplitBy] = field(
        default=None,
        metadata={
            "name": "SplitBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    tightness: Optional[TightnessValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )


@dataclass
class Arrangement(ArrangementT):
    """
    The vessel arrangement or capacity plan defined by its compartments.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class Panel(PanelT):
    """Structural concept of shipbuilding panels.

    Panels can typically be composed of plates, seams and stiffeners.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class VesselT(FormT):
    """
    Type definition of the Vessel asset subject to Classification.

    Attributes:
        coordinate_system: The vessel coordinate system definition. If
            not present, it is assumed that the Vessel is modelled in
            the global coordinate frame.
        classification_data:
        builder_information:
        tonnage_data:
        statutory_data:
        ship_designation:
        design_view:
        arrangement:
        reference_surfaces: Collection of frequently used surfaces which
            are referenced by more than one object. Will typically
            contain the outer shell definition.
        panel:
        plate:
        stiffener:
        bracket:
        pillar:
    """

    class Meta:
        name = "Vessel_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    coordinate_system: list[CoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "min_occurs": 1,
        },
    )
    classification_data: Optional[ClassificationData] = field(
        default=None,
        metadata={
            "name": "ClassificationData",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    builder_information: Optional[BuilderInformation] = field(
        default=None,
        metadata={
            "name": "BuilderInformation",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    tonnage_data: Optional[TonnageData] = field(
        default=None,
        metadata={
            "name": "TonnageData",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    statutory_data: Optional[StatutoryData] = field(
        default=None,
        metadata={
            "name": "StatutoryData",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    ship_designation: Optional[ShipDesignation] = field(
        default=None,
        metadata={
            "name": "ShipDesignation",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    design_view: list[DesignView] = field(
        default_factory=list,
        metadata={
            "name": "DesignView",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    arrangement: Optional[Arrangement] = field(
        default=None,
        metadata={
            "name": "Arrangement",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    reference_surfaces: Optional[ReferenceSurfaces] = field(
        default=None,
        metadata={
            "name": "ReferenceSurfaces",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    panel: list[Panel] = field(
        default_factory=list,
        metadata={
            "name": "Panel",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    plate: list[Plate] = field(
        default_factory=list,
        metadata={
            "name": "Plate",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    stiffener: list[Stiffener] = field(
        default_factory=list,
        metadata={
            "name": "Stiffener",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    bracket: list[Bracket] = field(
        default_factory=list,
        metadata={
            "name": "Bracket",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    pillar: list[Pillar] = field(
        default_factory=list,
        metadata={
            "name": "Pillar",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class Vessel(VesselT):
    """
    Vessel asset subject to Classification.
    """

    class Meta:
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )


@dataclass
class OcxXmlT(DocumentBaseT):
    """
    Root type of the schema.

    Attributes:
        vessel:
        class_catalogue: The Class catalogues provided as part of the
            OCX. The catalogue can hold the society's definitions of
            cross-sections, materials, hole shapes etc.
        units_ml:
        equipments:
    """

    class Meta:
        name = "ocxXML_T"
        target_namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )

    vessel: Optional[Vessel] = field(
        default=None,
        metadata={
            "name": "Vessel",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )
    class_catalogue: Optional[ClassCatalogue] = field(
        default=None,
        metadata={
            "name": "ClassCatalogue",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
            "required": True,
        },
    )
    units_ml: Optional[UnitsMl] = field(
        default=None,
        metadata={
            "name": "UnitsML",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "required": True,
        },
    )
    equipments: Optional[Equipments] = field(
        default=None,
        metadata={
            "name": "Equipments",
            "type": "Element",
            "namespace": "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd",
        },
    )


@dataclass
class OcxXml(OcxXmlT):
    """
    Root element of the schema.
    """

    class Meta:
        name = "ocxXML"
        namespace = (
            "https://3docx.org/fileadmin//ocx_schema//V310//OCX_Schema.xsd"
        )
