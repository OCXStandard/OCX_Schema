from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xml.etree.ElementTree import QName
from xsdata.models.datatype import XmlDateTime, XmlPeriod


class BarSectionTManufacture(Enum):
    ROLLED = "Rolled"
    WELDED = "Welded"


@dataclass
class BuilderInformationT:
    """
    Attributes
        yard: Name of the construction yard.
        designer: The name of the designer of the vessel.
        owner: Contractor of the vessel.
        year_of_build: Keel laying date.
    """
    class Meta:
        name = "BuilderInformation_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    yard: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    designer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    year_of_build: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "yearOfBuild",
            "type": "Attribute",
        }
    )


@dataclass
class ClassNotationT:
    """
    Type definition of ClassNotation.

    Attributes
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    hull: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    machinery: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ice_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "iceClass",
            "type": "Attribute",
        }
    )
    service_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceArea",
            "type": "Attribute",
        }
    )
    service_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "serviceFactor",
            "type": "Attribute",
        }
    )
    additional_notations: Optional[str] = field(
        default=None,
        metadata={
            "name": "additionalNotations",
            "type": "Attribute",
        }
    )


@dataclass
class ClassParametersT:
    """
    Information that specifies design and intended performance characteristics of
    the ship in accordance with classification society rules and statutory
    regulations (see ISO 10303-218, section 4.2.36).

    Attributes
        block_coefficient_class: The ratio of the moulded displacement
            volume to the volume of a block that has its length equal to
            the length class, its breadth equal to the moulded breadth
            and its depth equal to the scantlings draught (see ISO
            10303-218, section 4.2.32.1).
        design_speed_ahead: The forward speed at which the ship is
            designed to operate (see ISO 10303-218, section 4.2.32.2).
        design_speed_astern: The reverse speed at which the ship is
            designed to operate (see ISO 10303-218, section 4.2.32.3).
        length_solas: A length measurement for the ship measured in
            accordance with IMO IC110E (see ISO 10303-218, section
            4.2.32.5).
        lenght_class: A length measurement for the ship that is defined
            in classification society rules (see ISO 10303-218, section
            4.2.32.4).
        scantlings_draught: The summer load draught used by the
            classification society in its calculations for structural
            integrity and strength (see ISO 10303-218, section
            4.2.32.6).
    """
    class Meta:
        name = "ClassParameters_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    block_coefficient_class: Optional[float] = field(
        default=None,
        metadata={
            "name": "blockCoefficientClass",
            "type": "Attribute",
            "required": True,
        }
    )
    design_speed_ahead: Optional[float] = field(
        default=None,
        metadata={
            "name": "designSpeedAhead",
            "type": "Attribute",
        }
    )
    design_speed_astern: Optional[float] = field(
        default=None,
        metadata={
            "name": "designSpeedAstern",
            "type": "Attribute",
        }
    )
    length_solas: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthSolas",
            "type": "Attribute",
            "required": True,
        }
    )
    lenght_class: Optional[float] = field(
        default=None,
        metadata={
            "name": "lenghtClass",
            "type": "Attribute",
            "required": True,
        }
    )
    scantlings_draught: Optional[float] = field(
        default=None,
        metadata={
            "name": "scantlingsDraught",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Description:
    """Contains a description of the component its parent represents.

    The description is stored as a string. You can use this element for
    whatever purposes you require. This element can be used inside many
    OCX XML elements but is optional.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DescriptionT:
    class Meta:
        name = "Description_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class EntityRefBaseT:
    """Abstract base class for defining a reference to an entity.

    All entity reference elements should be based on this type.

    Attributes
        local_ref: A rference to a unique ID within the scope of this
            XML file. Ether a localRef or a GUIDRef shall be provided,
            or both. The schema will check this by the assertion:
            test="(@localRef and not(@ocx:GUIDRef)) or (not(@localRef)
            and @ocx:GUIDRef) or (@localRef and @ocx:GUIDRef)".
        guidref: A globally unique ID referring to an entity in the
            authoring application. The sending application creates and
            holds the GUID. Used to establish a unique reference to an
            entity persistent  between applications.  Ether a localRef
            or a GUIDRef shall be provided, or both. The schema will
            check this by the assertion: test="(@localRef and
            not(@ocx:GUIDRef)) or (not(@localRef) and @ocx:GUIDRef) or
            (@localRef and @ocx:GUIDRef)".
    """
    class Meta:
        name = "EntityRefBase_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    local_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "localRef",
            "type": "Attribute",
        }
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class HeaderT:
    """
    Type definition for the Header information for an XML instance.

    Attributes
        time_stamp: Time stamp of the instance.
        name: Name of the XML instance.
        author: Name of author.
        organization: Name of originating organization.
        application_version: Version of originating application.
        originating_system: Name of originating system or application.
        documentation: Documentation of the content of the XML file.
    """
    class Meta:
        name = "Header_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    application_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    originating_system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class IdBaseT:
    """
    Abstract base type for all types which need to carry an ID.

    Attributes
        id: An identifier for an element unique within the scope of the
            XML file. Each id must be unique within a document. The
            attribute uses the standard XML 1.0 ID type as defined in
            the XML Schema specification. This attribute is required in
            many OCX XML elements and an application should generate
            them automatically.
    """
    class Meta:
        name = "IdBase_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class KnotVectorT:
    """
    Type definition of the NURBS knot vector.

    Attributes
        value: The list of knots separated by  white space. Knots must
            pe provided in increasing order.
    """
    class Meta:
        name = "KnotVector_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class QuantityT:
    """Type definition of the abstract base class for all types with values carrying a Unit : Q = v * u.

    Attributes
        numericvalue: The numerical value of the quantity.
        unit: The reference to the unitsML reference unit.
    """
    class Meta:
        name = "Quantity_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    numericvalue: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ReferencePlaneT:
    """
    Type definition of the concept of a reference plane which is typically used to
    define an unbounded geometry.
    """
    class Meta:
        name = "ReferencePlane_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ReferenceT:
    """
    Attributes
        element: The name of the changed schema element.
        location_ref: A reference locator to the changed element.
    """
    class Meta:
        name = "Reference_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    element: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    location_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "locationRef",
            "type": "Attribute",
        }
    )


@dataclass
class ShipDesignationT:
    """The different types of identification given to the ship in order that it can
    be categorised by any shipping related organisation.

    It contains the minimal information which might be available about
    the ship.

    Attributes
        ship_name: The name of the ship assigned by the owner.
        call_sign: The unique life-cycle identifier assigned to the ship
            by the flag state for radio communication.
        number_imo: A unique identification of a vessel according to IMO
            resolution A.600(15). It is made of the three letters “IMO”
            in front of the Lloyd’s Register number. This is a unique
            seven digit number that is assigned to propelled, sea-going
            merchant ships of 100 GT and above upon keel laying (with
            some exceptions), see: IACS Procedural Requirements No. 11,
            IACS Procedure for Assigning Date of Build, 1996
            href="http://www.imo.org/Facilitation/mainframe.asp?topic_id=388"&gt;Information
            on IMO ship identification number scheme on the web site of
            the IMO (last visited: 2005-09-05).
        ship_type: Optional string indicating the ship type.
    """
    class Meta:
        name = "ShipDesignation_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ship_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipName",
            "type": "Attribute",
            "required": True,
        }
    )
    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Attribute",
        }
    )
    number_imo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberIMO",
            "type": "Attribute",
        }
    )
    ship_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipType",
            "type": "Attribute",
        }
    )


class SlotParametersTSlotType(Enum):
    SLIT = "Slit"
    OPEN = "Open"


@dataclass
class StatutoryDataT:
    """
    Type definition of vessel data related to the flag state.

    Attributes
        port_registration: The national home port of the ship. The port
            of registration lies within the jurisdiction of the flag
            state (see ISO 10303-215, section 4.2.142.5).
        flag_state: The national authority with which the ship is
            registered (see ISO 10303-215, section 4.2.142.3).
    """
    class Meta:
        name = "StatutoryData_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    port_registration: Optional[str] = field(
        default=None,
        metadata={
            "name": "portRegistration",
            "type": "Attribute",
        }
    )
    flag_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "flagState",
            "type": "Attribute",
        }
    )


@dataclass
class Vector3DT:
    """
    Type definition of a unit vector.

    Attributes
        x: Numeric value of x component.
        y: Numeric value of y component.
        z: Numeric value of z component.
    """
    class Meta:
        name = "Vector3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class BulkCargoTypeValue(Enum):
    """
    Attributes
        CEMENT: The bulk cargo is cement.
        COAL: The bulk cargo is coal.
        FISH: The bulk cargo is fish.
        GENERAL: The bulk cargo is of ageneral,non-specific type.
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

    Attributes
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
        LR: Lloyd's Register.
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
        TL: Türk Loydu Vakfi.
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
    Attributes
        CARGO: A compartment is designed to carry liquid, bulk, or
            containerized goods.
        BALLAST: The compartment is a watertight compartment to hold
            water ballast.
        FRESHWATER: The compartment is a watertight compartment to hold
            fresh water.
        FUEL: The compartment is a watertight compartment to hold fuel.
        MACHINERY: The compartment is designed to contain machinery for
            the operation of the ship or in support of its mission.
        VOID: The compartment is designed as an inaccessible, closed
            space that is never used to carry cargo or to be regularly
            occupied by humans.  The main uses of a void compartment are
            segregating the cargo and fluids that are necessary to
            operate the ship, or to provide emergency access to other
            spaces.
        OTHER: Storage of equipment, e.g. ropes.
        LUBE: The compartment is a watertight compartment to hold fresh
            lube oil.
        PASSAGEWAY: The compartment is designe for use as passageway.
        ACCESS: The compartment is designed to be used for access.
        MISCELLANEOUS: Storage of miscellaneous fluids, e.g.sewage.
    """
    CARGO = "Cargo"
    BALLAST = "Ballast"
    FRESHWATER = "Freshwater"
    FUEL = "Fuel"
    MACHINERY = "Machinery"
    VOID = "Void"
    OTHER = "Other"
    LUBE = "Lube"
    PASSAGEWAY = "Passageway"
    ACCESS = "Access"
    MISCELLANEOUS = "Miscellaneous"


class CurveFormEnum(Enum):
    """
    Enumerator of NURBS curve forms.

    Attributes
        UNKNOWN: An unknown curve form.
        OPEN: An open curve form.
        CLOSED: A closed curve form with C0 continuity.
        PERIODIC: A closed curve form wit C1 continuity.
    """
    UNKNOWN = "Unknown"
    OPEN = "Open"
    CLOSED = "Closed"
    PERIODIC = "Periodic"


class EdgeReinforcementValue(Enum):
    """
    Attributes
        FLANGED: The bracket edge has a flanged stiffening with a bend
            radius.
        FACE_PLATE: The bracket edge has a face plate.
        BUCKLING_STIFFENER: The bracket edge has a buckling stiffener.
    """
    FLANGED = "Flanged"
    FACE_PLATE = "FacePlate"
    BUCKLING_STIFFENER = "BucklingStiffener"


class FreeboardTypeValue(Enum):
    """
    Attributes
        A: A type "A" ship is one which is designed to carry only liquid
            cargoes in bulk, and in which cargo tanks have only small
            access openings closed by watertight gasketed covers of
            steel or equivalent material.
        B: All ships which do not come within the provisions regarding
            Type "A" ships shall be considered as Type "B" ships. .
    """
    A = "A"
    B = "B"


class FunctionTypeValue(Enum):
    """
    Attributes
        BRACKET: A supporting plate.
        BRACKET_END_BRACKET: A bracket attached to the end of stiffener.
        BRACKET_TRIPPING: A bracket used to support a load bearing
            element in between primary supporting memebers.
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
        DECK_WEATEHER_DECK: Weather deck is normally the uppermost
            complete deck exposed to weather and sea, which has
            permanent means of closing all exposed openings.
        DECK_FORECASTLE_DECK: Forecastle deck is a the deck attached to
            the short superstructure situated at the bow.
        DECK_FREEBOARD_DECK: Freeboard deck is the first deck abowe the
            waterline.
        DECK_GIRDER: Deck Structure is the deck plating with primary
            girder memebers.
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
            on the freeboard deck extending for at least 92% of the
            breadth of the ship.
        DECK_TRUNK_DECK: Deck Structure is the deck plating with
            stiffeners, girders and supporting pillars.
        DECK_TWEEEN_DECK: Tween Decks is an abbreviation of between
            decks, placed between the upper deck and the tank top in the
            cargo holds.
        DECK_WEELHOUSE_DECK: Deck House is a structure on the freeboard
            or superstructure deck not extending from side to side of
            the ship.
        FOUNDATION: Supporting foundation structure .
        FOUNDATION_ENGINE: Engine foundation including foundation top
            plate .
        HATCHWAY_COAMING: Hatch Coaming is the vertical plating built
            around the hatchways to prevent water from entering the
            hold; and to serve as a framework for the hatch covers.
        HATCHWAY_COAMING_END_COAMING: Hatch Coaming is the vertical
            plating built around the hatchways to prevent water from
            entering the hold; and to serve as a framework for the hatch
            covers.
        HATCHWAY_COAMING_SIDE_COAMING: Hatch Coaming is the vertical
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
            penetrating a primary supporting memeber.
        PLATING_GUSSET: Gusset is a triangular plate, usually fitted to
            distribute forces at a strength connection between two
            structural members.
        PLATING_SHEDDER: Shedder Plates are slanted plates fitted in dry
            cargo holds to prevent undesired pockets of cargo. The term
            is also commonly applied to slanted plates that are fitted
            to improve the structural stability of corrugated bulkheads
            and framing members.&gt;.
        SHEER_STRAKE: Sheer Strake is the top strake of a ship's side
            shell plating&gt;.
        SHELL: The watertight shell plating of the hull.
        SHELL_BILGE_KEEL: Bilge Keel is a piece of plate set
            perpendicular to a ship’s shell along her bilges for about
            one third her length to reduce rolling.&gt;.
        SHELL_BILGE_STRAKE: Bilge Strake is the strake at the turn of
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
            freeboard deck extending for at least 92% of the breadth of
            the ship. Often named deckhouse or wheelhouse.
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
        TRANSVERSAL_BULKHEAD_PARTIAL: A partial trnsverse bulkead
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
        WEB_FRAME_GENERAL_WEBFRAME: A transverse stiffening system.
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
    DECK_WEATEHER_DECK = "DECK: Weateher deck"
    DECK_FORECASTLE_DECK = "DECK: Forecastle deck"
    DECK_FREEBOARD_DECK = "DECK: Freeboard deck"
    DECK_GIRDER = "DECK: Girder"
    DECK_INNER_BOTTOM_DECK = "DECK: Inner bottom deck"
    DECK_PLATFORM_DECK = "DECK: Platform deck"
    DECK_POOP_DECK = "DECK: Poop deck"
    DECK_STRENGTH_DECK = "DECK: Strength deck"
    DECK_SUPERSTRUCTURE_DECK = "DECK: Superstructure deck"
    DECK_TRUNK_DECK = "DECK: Trunk deck"
    DECK_TWEEEN_DECK = "DECK: Tweeen deck"
    DECK_WEELHOUSE_DECK = "DECK: Weelhouse deck"
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
    LONGITUDINAL_CENTERLINE_SIDE_GIRDER = "LONGITUDINAL: Centerline side girder"
    LONGITUDINAL_DOUBLE_BOTTOM = "LONGITUDINAL: Double bottom"
    LONGITUDINAL_TOP_TANK = "LONGITUDINAL: Top tank"
    LONGITUDINAL_HOPPER_SIDE_LOWER = "LONGITUDINAL: Hopper side lower"
    LONGITUDINAL_HOPPER_SIDE_UPPER = "LONGITUDINAL: Hopper side upper"
    LONGITUDINAL_INNER_BOTTOM = "LONGITUDINAL: Inner bottom"
    LONGITUDINAL_LOWER_STOOL_BOTTOM_PLATE = "LONGITUDINAL: Lower stool bottom plate"
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
    WEB_FRAME_GENERAL_WEBFRAME = "WEB_FRAME: General webframe"
    WEB_FRAME_HORIZONTAL = "WEB_FRAME: Horizontal"
    WEB_FRAME_VERTICAL = "WEB_FRAME: Vertical"
    WEB_FRAME_MAIN_FRAME = "WEB_FRAME: Main frame"
    WEB_FRAME_TOPSIDE_TANK = "WEB_FRAME: Topside tank"
    WEB_FRAME_SIDE = "WEB_FRAME: Side"
    WEB_FRAME_TWEEN_DECK_FRAME = "WEB_FRAME: Tween deck frame"


class GeometryFormatValue(Enum):
    """
    Attributes
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
    Attributes
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
    Attributes
        ALCOHOL: The cargo is alcohol.
        AMMONIA: The cargo is ammonia.
        ASPHALT: The cargo is asphalt.
        AVIATION_OIL: The cargo is aviation oil.
        CAUSTIC_SODA: The cargo is caustic soda.
        CEMENT: The cargo is liquid cement.
        CHEMICHAL: The cargo is a liquid chemical.
        CRUDE_OIL: The cargo is crude oil.
        EDIBLE_OIL: The cargo is deible oil.
        FUEL_OIL: The cargo is fuel oil.
        FRESH_WATER: The cargo is fresh water.
        HYDROCLORID_ACID: The cargo is hydroclorid acid.
        LUBRICATIONG_OIL: The cargo is lubrication oil.
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
    CHEMICHAL = "chemichal"
    CRUDE_OIL = "crude oil"
    EDIBLE_OIL = "edible oil"
    FUEL_OIL = "fuel oil"
    FRESH_WATER = "fresh water"
    HYDROCLORID_ACID = "hydroclorid acid"
    LUBRICATIONG_OIL = "lubricationg oil"
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


class PositionValue(Enum):
    """
    Attributes
        NEAR_SIDE: The bracket is at the near side of a penetration.
        FAR_SIDE: The bracket is at the far side of a penetration.
    """
    NEAR_SIDE = "Near side"
    FAR_SIDE = "Far side"


class RefTypeValue(Enum):
    """
    Allowable OCX types which can be referenced using the ocxItemPtr.

    Attributes
        OCX_PANEL: A reference to an instantiated  structure composision
            of type Panel.
        OCX_PLATE: A reference to an instantiated structure part of type
            Plate.
        OCX_SEAM: A reference to an instantiated structurecomposision of
            type Seam.
        OCX_BRACKET: A reference to an instantiated structure part of
            type Bracket.
        OCX_STIFFENER: A reference to an instantiated structure part of
            type Stiffener.
        OCX_PILLAR: A reference to an instantiated structure part of
            type Pillar.
        OCX_CONNECTION_CONFIGURATION: A reference to an instantiated
            stiffener configuration.
        OCX_HOLE2_D: A reference to a catalogue 2D hole shape.
        OCX_GRID_REF: A reference to a frame table grid position.
        OCX_MATERIAL: A reference to a catalogue material.
        OCX_BAR_SECTION: A reference to a catalogue bar section.
        OCX_CELL: A reference to an instantiated compartment cell.
        OCX_VESSEL: A reference to the vessel instance.
        OCX_FREE_EDGE_CURVE3_D: A reference to an instantiated free edge
            geometry.
        OCX_SURFACE: A reference to an instantiated surface.
        OCX_END_CUT: A reference to a stiffener end cut.
        OCX_OCCURENCE_GROUP: A reference to an occurrence group in a
            design view.
        OCX_EDGE_REINFORCEMENT:
        OCX_HOLE2_DCONTOUR:
    """
    OCX_PANEL = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Panel")
    OCX_PLATE = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Plate")
    OCX_SEAM = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Seam")
    OCX_BRACKET = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Bracket")
    OCX_STIFFENER = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Stiffener")
    OCX_PILLAR = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Pillar")
    OCX_CONNECTION_CONFIGURATION = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}ConnectionConfiguration")
    OCX_HOLE2_D = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Hole2D")
    OCX_GRID_REF = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}GridRef")
    OCX_MATERIAL = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Material")
    OCX_BAR_SECTION = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}BarSection")
    OCX_CELL = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Cell")
    OCX_VESSEL = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Vessel")
    OCX_FREE_EDGE_CURVE3_D = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}FreeEdgeCurve3D")
    OCX_SURFACE = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Surface")
    OCX_END_CUT = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}EndCut")
    OCX_OCCURENCE_GROUP = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}OccurenceGroup")
    OCX_EDGE_REINFORCEMENT = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}EdgeReinforcement")
    OCX_HOLE2_DCONTOUR = QName("{http://data.dnvgl.com/Schemas/ocxXMLSchema}Hole2DContour")


class TightnessValue(Enum):
    """
    Attributes
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
    Attributes
        AIRCRAFT: The unit cargo is aircraft.
        BOAT: The unit cargo is boat.
        CABLE: The unit cargo is cable.
        CONTAINER: The unit cargo is container.
        DRUMS: The unit cargo is drums.
        LIVESTOCK: The unit cargo is livestock.
        PALLET: The unit cargo is pallet.
        TRAILER: The unit cargo is tariler.
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


class LangValue(Enum):
    VALUE = ""


@dataclass
class AmountOfSubstanceType:
    """
    Type of the quantity amount of substance.

    Attributes
        symbol: Symbol of the quantity amount of substance.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="N",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class ElectricCurrentType:
    """
    Type of the quantity electric current.

    Attributes
        symbol: Symbol of the quantity electric current.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="I",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


class EnumeratedRootUnitTypePrefix(Enum):
    """
    Attributes
        Y: yotta: septillion
        Z: zetta: sextillion
        P: exa: quintillion
        T: peta: quadrillion
        G: tera: trillion
        M: giga: billion
        K: mega: million
        H: kilo: thousand
        DA: hecto: hundred
        D: deca: ten
        C: deci: tenth
        M_1: centi: hundredth
        U: milli: thousandth
        N: micro: millonth
        P_1: nano: billonth
        F: pico: trillionth
        A: femto: quadrillionth
        Z_1: atto: quintillionth
        Y_1: zepto: sextillionth:
        KI: yocto: septillionth
        MI: kibi: kilobinary
        GI: mebi: magabinary
        TI: gibi: gigabinary
        PI: tebi: terabinary
        EI: exbi: exabinary
        ZI: pebi: petabinary
        YI: yobi: yottabinary
    """
    Y = "Y"
    Z = "Z"
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
    U = "u"
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
    PI = "Pi"
    EI = "Ei"
    ZI = "Zi"
    YI = "Yi"


class EnumeratedRootUnitTypeUnit(Enum):
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
    ATOMIC_UNIT_OF_1ST_HYPERPOLARIZABLITY = "atomic_unit_of_1st_hyperpolarizablity"
    ATOMIC_UNIT_OF_2ND_HYPERPOLARIZABLITY = "atomic_unit_of_2nd_hyperpolarizablity"
    ATOMIC_UNIT_OF_ACTION = "atomic_unit_of_action"
    ATOMIC_UNIT_OF_CHARGE = "atomic_unit_of_charge"
    ATOMIC_UNIT_OF_CHARGE_DENSITY = "atomic_unit_of_charge_density"
    ATOMIC_UNIT_OF_CURRENT = "atomic_unit_of_current"
    ATOMIC_UNIT_OF_ELECTRIC_DIPOLE_MOMENT = "atomic_unit_of_electric_dipole_moment"
    ATOMIC_UNIT_OF_ELECTRIC_FIELD = "atomic_unit_of_electric_field"
    ATOMIC_UNIT_OF_ELECTRIC_FIELD_GRADIENT = "atomic_unit_of_electric_field_gradient"
    ATOMIC_UNIT_OF_ELECTRIC_POLARIZABLITY = "atomic_unit_of_electric_polarizablity"
    ATOMIC_UNIT_OF_ELECTRIC_POTENTIAL = "atomic_unit_of_electric_potential"
    ATOMIC_UNIT_OF_ELECTRIC_QUADRUPOLE_MOMENT = "atomic_unit_of_electric_quadrupole_moment"
    ATOMIC_UNIT_OF_ENERGY = "atomic_unit_of_energy"
    ATOMIC_UNIT_OF_FORCE = "atomic_unit_of_force"
    ATOMIC_UNIT_OF_LENGTH = "atomic_unit_of_length"
    ATOMIC_UNIT_OF_MAGNETIC_DIPOLE_MOMENT = "atomic_unit_of_magnetic_dipole_moment"
    ATOMIC_UNIT_OF_MAGNETIC_FLUX_DENSITY = "atomic_unit_of_magnetic_flux_density"
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
    NATURAL_UNIT_OF_MOMENTUM_IN_ME_V_PER_C = "natural_unit_of_momentum_in_MeV_per_c"
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

    Attributes
        symbol: Symbol of the quantity length.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="L",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class LuminousIntensityType:
    """
    Type of the quantity luminous intensity.

    Attributes
        symbol: Symbol of the quantity luminous intensity.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="J",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class MassType:
    """
    Type of the quantity mass.

    Attributes
        symbol: Symbol of the quantity mass.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="M",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class SymbolType:
    """Type for symbols.

    Used in units, quantities, and prefixes.

    Attributes
        type_value: Type of symbol representation.  Examples include
            ASCII, unicode, HTML, and MathML.
        content:
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class ThermodynamicTemperatureType:
    """
    Type of the quantity thermodynamic temperature.

    Attributes
        symbol: Symbol of the quantity thermodynamic temperature.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="Θ",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class TimeType:
    """
    Type of the quantity time.

    Attributes
        symbol: Symbol of the quantity time.
        power_numerator: An integer exponent of the unit.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    symbol: str = field(
        init=False,
        default="T",
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class ApPos(QuantityT):
    """
    X Position of AP.
    """
    class Meta:
        name = "AP_Pos"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class AirPipeHeight(QuantityT):
    """
    The AirpipeHeight specifies height from the base line to the top of the air
    pipe, if any.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class AngleOfRepose(QuantityT):
    """
    The natural angle of repose specifies the angle naturally subtended with the
    horizontal by the upper surface of the conic pile, made by the bulk cargo when
    loaded into a hold by a chute using gravity alone.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class AngleTolerance(QuantityT):
    """
    Absolute angular tolerance measure used by the exporting application when
    defining geometry.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ApplicationRefT(EntityRefBaseT):
    """
    The ApplicationRef type relates the parent element back to the owning entity in
    the source application (external reference type).
    """
    class Meta:
        name = "ApplicationRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    external_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Area(QuantityT):
    """The surface area computed by the sending application.

    Used to verify geometry reconstruction by allowing the receiving
    application to compare the source value with the reconstructed
    value.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ArmLengthU(QuantityT):
    """
    The length of the bracket in local U-direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ArmLengthV(QuantityT):
    """
    The length of the bracket in local V-direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Axis(Vector3DT):
    """
    Cylinder revolution axis direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BaseRadius(QuantityT):
    """
    Cone base radius.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BlockCoefficient(QuantityT):
    """
    The ratio of the moulded displacement volume to the volume of a block that has
    its length equal to the length class, its breadth equal to the moulded breadth
    and its depth equal to the scantlings draught (see ISO 10303-218, section
    4.2.32.1).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BracketRefT(EntityRefBaseT):
    """
    Type definition of A OcxItemPtr reference to a Bracket instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "BracketRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_BRACKET,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class BuilderInformation(BuilderInformationT):
    """The organization that designs, builds, maintains, and repairs ships.

    This type contains information about the ship, which is specific in
    the context of the shipyard, in which it has been built.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulbAngle(QuantityT):
    """
    Profile width and web thickness.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulbBottomRadius(QuantityT):
    """
    The radius at the bottom of the web.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulbInnerRadius(QuantityT):
    """
    The inner radius of the bulb.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulbOuterRadius(QuantityT):
    """
    The outer radius of the bulb.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulbTopRadius(QuantityT):
    """
    The radius at the top of the bulb.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CarriagePressure(QuantityT):
    """
    The CarriagePressure specifies the required pressure of the compartment in
    which the cargo is to be carried.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ChildRefT(EntityRefBaseT):
    """
    Type definition of a child instance in a ProductView.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "ChildRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: Optional[RefTypeValue] = field(
        default=None,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class ClassNotation(ClassNotationT):
    """
    The notations given to the hull and machinery of the Ship by the classification
    society as a result of its approval activities during the design, manufacture
    and in-service maintenance of the ship (see ISO 10303-218, section 4.2.35).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ConnectionLength(QuantityT):
    """
    The connection length of the direct connection between a stiffener and a
    primary supporting memeber.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CopeHeight(QuantityT):
    """
    The height of the cope.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CopeLength(QuantityT):
    """The length of the cope.

    (The default is CopeLength=CopeRadius)
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CopeRadius(QuantityT):
    """
    The cope or heel radius.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CutbackDistance(QuantityT):
    """
    Distance from stiffener logical end position to the start of the web cutback.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DeadWeight(QuantityT):
    """
    The weight of the passengers, crew, cargo, stores, ballast, fresh water, fuel
    oil, and other consumables being carried by a ship (see ISO 10303-215, section
    4.2.74).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DeepestEquilibriumWl(QuantityT):
    """
    Deepest equilibrium waterline in damaged condition.
    """
    class Meta:
        name = "DeepestEquilibriumWL"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Density(QuantityT):
    """
    The material density.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DescriptionBaseT(IdBaseT):
    """
    Abstract base element for all elements that needs to carry a description.

    Attributes
        description:
        name: An optional descriptive or display name.
    """
    class Meta:
        name = "DescriptionBase_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DesignSpeed(QuantityT):
    """
    The forward or service speed at which the ship is designed to operate (see ISO
    10303-218, section 4.2.32.2).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Diameter(QuantityT):
    """
    Circle diameter.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Displacement(QuantityT):
    """The Radius displacement outside the original corner of the rectangle.

    If left out (or set to zero), the radius passes through the original
    corner of the rectangle.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DistanceAbove(QuantityT):
    """
    The distance of the lug above the plate (bottom of the slot opening).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DistanceBelow(QuantityT):
    """
    The distance below the lug plate to bottom of the slot.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DistanceToAp(QuantityT):
    """
    If #0/FR0 (FR0 has  per definition ReferenceLocation=0) is not located at AP,
    give the offset here (positive or negative distance).
    """
    class Meta:
        name = "DistanceToAP"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DistanceTolerance(QuantityT):
    """
    Absolute tolerance measure used by the exporting application when defining
    geometry.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DryWeight(QuantityT):
    """
    The total dry weight of the parent member.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class EdgeCurveRefT(EntityRefBaseT):
    """
    Type definition of the EdgeCurveRef.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "EdgeCurveRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: Optional[RefTypeValue] = field(
        default=None,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class EndCutRefT(EntityRefBaseT):
    """
    The type of the EndCutRef.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "EndCutRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_END_CUT,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class ExternalGeometryRefT:
    """
    The ExternalGeometryRef_ defintion  of an element  used to point to an external
    geometry representation  of the parent  entity (e.g. Plate, Stiffener, Bracket,
    Memeber ).
    """
    class Meta:
        name = "ExternalGeometryRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    external_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    geometry_format: GeometryFormatValue = field(
        init=False,
        default=GeometryFormatValue.STP,
        metadata={
            "name": "geometryFormat",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class FpPos(QuantityT):
    """X-Position of fwd.

    end of waterline for free-board length.
    """
    class Meta:
        name = "FP_Pos"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FilletRadius(QuantityT):
    """
    Corner fillet radius.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FillingHeight(QuantityT):
    """
    The filling_height specifies the maximum height for filling of the tank
    compartment.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlangeCutBackAngle(QuantityT):
    """
    Cut angle of stiffener flange.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlangeDirection(Vector3DT):
    """Direction of the stiffener flange.

    Not required for symmetrical profiles.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlangeNoseHeight(QuantityT):
    """
    Nose height of sniped stiffener flange.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlangeThickness(QuantityT):
    """
    The thickness of the flange.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlangeWidth(QuantityT):
    """
    Section profile flange width.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FreeEdgeRadius(QuantityT):
    """The edge radius at the bracket free edge.

    Assumed to be straight if no radius value is provided.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FreeboardDeckHeight(QuantityT):
    """
    The height of free-board deck, D1.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FreeboardLength(QuantityT):
    """
    The free-board length of the Vessel, Lll.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class GridPosition(QuantityT):
    """
    The position of the first grid in the spacing group along the grid axis.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Header(HeaderT):
    """
    The header information of an XML export.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class HeavyBallastDraught(QuantityT):
    """
    The Vessel draught at heavy ballast, Thb.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Height(QuantityT):
    """
    The height of the parent element.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class HoleRefT(EntityRefBaseT):
    """
    Type definition of A OcxItemPtr reference to a Bracket instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "HoleRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_HOLE2_D,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class InertiaU(QuantityT):
    """
    Moment of inertia around NeutralAxisU.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class InertiaV(QuantityT):
    """
    Moment of inertia around NeutralAxisV.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class KnotVector(KnotVectorT):
    """The knot-vector is a list of  size m=+n-1 knots where p is the polynomial
    basis degree and n is the number of control points.

    The knot vector consists of a non-decreasing sequence of values.
    Knot multiplicities can be included. A knot multiplicity means that
    a knot value can be repeated up to p+1 times.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LengthOfWaterline(QuantityT):
    """
    The length of the waterline at T, Lwl.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Length2(QuantityT):
    """The curve length computed by the sending application.

    Used to verify geometry reconstruction.
    """
    class Meta:
        name = "Length"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LowerRadius(QuantityT):
    """
    The lower radious of an opening or slot.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Lpp(QuantityT):
    """
    The length of the Vessel between perpendiculars, Lpp.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MajorAxis(Vector3DT):
    """
    Direction of ellipse major axis.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MajorDiameter(QuantityT):
    """
    The ellipse major diameter.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MaterialRefT(EntityRefBaseT):
    """
    Material pointer type.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "MaterialRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_MATERIAL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class MinorAxis(Vector3DT):
    """
    Definition of the ellipse minor axis direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MinorDiameter(QuantityT):
    """
    The ellipse minor diameter.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MouldedBreadth(QuantityT):
    """
    The moulded breadth of the Vessel, B.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MouldedDepth(QuantityT):
    """
    The moulded depth of the Vessel, D.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class NurbspropertiesT:
    """
    Type definition of a class defining the properties of the NURBS curve.

    Attributes
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    num_ctrl_pts: Optional[int] = field(
        default=None,
        metadata={
            "name": "numCtrlPts",
            "type": "Attribute",
            "required": True,
        }
    )
    num_knots: Optional[int] = field(
        default=None,
        metadata={
            "name": "numKnots",
            "type": "Attribute",
            "required": True,
        }
    )
    form: CurveFormEnum = field(
        default=CurveFormEnum.OPEN,
        metadata={
            "type": "Attribute",
        }
    )
    is_rational: bool = field(
        default=False,
        metadata={
            "name": "isRational",
            "type": "Attribute",
        }
    )


@dataclass
class NeutralAxisU(Vector3DT):
    """Position of the neutral axis parallel to the U axis measured from the foot
    point.

    The U axis is along the flange.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class NeutralAxisV(Vector3DT):
    """Position of the neutral axis parallel to the V axis measured from the mould
    line side.

    The V axis is along the web.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Normal(Vector3DT):
    """
    A unit normal vector to a surface.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class NormalBallastDraught(QuantityT):
    """
    The Vessel draught at normal ballast, Tnb.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Offset(QuantityT):
    """An offset from a reference plane or surface.

    A possitive offset value is in the direction of the surface normal
    vector.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OffsetU(QuantityT):
    """
    The offset from stiffener trace line of cross section in local U direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OffsetV(QuantityT):
    """
    The offset from stiffener trace-line of cross section in local V direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Overshoot(QuantityT):
    """The overshoot of the flange beyond the web.

    Shall be included in the Width..
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Permeability(QuantityT):
    """
    The permeability specifies the amount by which the Cargo takes up water.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PoissonRatio(QuantityT):
    """
    The material Poisson ration.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PrimaryAxis(Vector3DT):
    """
    The unit vector of the local X-axis (U-Axis) given in global Coordinate System.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Radius(QuantityT):
    """
    The radius of the parent element.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RectangularTubeT:
    """
    Attributes
        height: Profile outer diameter.
        width: Profile width.
        thickness: Wall thickness.
    """
    class Meta:
        name = "RectangularTube_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    thickness: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Reference(ReferenceT):
    """
    A reference to the schema type which is affected by this change to the schema.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ReferenceLocation(QuantityT):
    """
    Location on the reference axis.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ReliefValvePressure(QuantityT):
    """
    Pressure valve opening pressure when exceeding the general value.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RootRefT(EntityRefBaseT):
    """
    Type definition of the root element in a design view.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "RootRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: Optional[RefTypeValue] = field(
        default=None,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class RuleLength(QuantityT):
    """Rule (scantling) length, L.

    A length measurement for the ship that is defined in classification
    society rules (see ISO 10303-218, section 4.2.32.4).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ScantlingDraught(QuantityT):
    """Design draught moulded, fully loaded condition, Td.

    The summer load draught used by the classification society in its
    calculations for structural integrity and strength (see ISO
    10303-218, section 4.2.32.6).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SecondaryAxis(Vector3DT):
    """
    The unit vector of the local Y-axis (V-Axis) given in global Coordinate System.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SectionRefT(EntityRefBaseT):
    """
    Section pointer type.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "SectionRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_BAR_SECTION,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class ShipDesignation(ShipDesignationT):
    """The different types of identification given to the ship in order that it can
    be categorised by any shipping related organisation.

    It contains the minimal information which might         be available
    about the ship.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SlammingDraughtEmptyFp(QuantityT):
    """
    The design slamming draught at FP (all ballast tanks empty), Tf-e.
    """
    class Meta:
        name = "SlammingDraughtEmptyFP"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SlammingDraughtFullFp(QuantityT):
    """
    The Vessel draught at FP used when calcualtion design slamming loads (all
    ballast tanks full), Tf-f.
    """
    class Meta:
        name = "SlammingDraughtFullFP"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Spacing(QuantityT):
    """
    The grid spacing of the spacing group.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SpeedFactor(QuantityT):
    """
    Speed factor Cav.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Start(QuantityT):
    """
    The location of Fram#0 in the frame table.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StatutoryData(StatutoryDataT):
    """
    The vessel statutory information.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StowageFactor(QuantityT):
    """The StowageFactor specifies the average specific volume for a dry cargo.

    The stowage factor is usually expressed as the volume in cubic
    meters that is occupied by one metric ton of the cargo.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StowageHeight(QuantityT):
    """Z coordinate of dry bulk stowage height.

    If not specified, top of cargo room will be used.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ThermalExpansionCoefficient(QuantityT):
    """
    The material thermal expansion coefficient.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Thickness(QuantityT):
    """
    The thickness of the parent element.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class TipRadius(QuantityT):
    """
    Cone base radius.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Tonnage(QuantityT):
    """
    She numerical value resulting from the tonnage calculation (see ISO 10303-215,
    section 4.2.165.3).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class TorsionConstant(QuantityT):
    """
    The torsional constant is calculated from the cross-section and determines the
    torsional rigidity together with the shear modulus.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Udirection(Vector3DT):
    """
    Local U deirection in a local coordinate system.
    """
    class Meta:
        name = "UDirection"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UknotVector(KnotVectorT):
    """The knot-vector in U direction is a list of  size m=+n-1 knots where p is
    the polynomial basis degree and n is the number of control points.

    The knot vector consist of a non-decreasing sequence of values. Knot
    multiplicities can be included. A knot multiplicity means that a
    knot value can be repeated up to p+1 times.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UltimateStress(QuantityT):
    """
    The material ultimate strsss.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UnitCargoT:
    """
    Type definition of dry cargo properties, reference is made to ISO
    10303-215:2004.
    """
    class Meta:
        name = "UnitCargo_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    unit_cargo_type: Optional[UnitCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "unitCargoType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Unose(QuantityT):
    """
    The bracket nose depth at the local U end of the bracket.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UpperDeckArea(QuantityT):
    """
    Projected area of upper deck forward 0.2 L.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UpperRadius(QuantityT):
    """
    The upper radius of an ipening or a slot.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UserDefinedParameterT(QuantityT):
    class Meta:
        name = "UserDefinedParameter_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Vdirection(Vector3DT):
    """
    Local V direction in a local coordinate system.
    """
    class Meta:
        name = "VDirection"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Vector3D(Vector3DT):
    """
    Unit vector of length 1.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class VknotVector(KnotVectorT):
    """The knot-vector in V direction is a list of  size m=+n-1 knots where p is
    the polynomial basis degree and n is the number of control points.

    The knot vector consist of a non-decreasing sequence of values. Knot
    multiplicities can be included. A knot multiplicity means that a
    knot value can be repeated up to p+1 times.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Vnose(QuantityT):
    """
    The bracket nose depth at the local V end of the bracket.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Volume(QuantityT):
    """
    The volume of a compartment or space.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WaterPlaneArea(QuantityT):
    """
    The area of water-plane forward 0.2 L at scantling draught Td.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebCutBackAngle(QuantityT):
    """
    Sniped angle of stiffener web.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebDirection(Vector3DT):
    """
    Direction of the stiffener web.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebNoseHeight(QuantityT):
    """
    Nose height of sniped stiffener web.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebThickness(QuantityT):
    """
    The thickness of the web.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Width(QuantityT):
    """
    The width of the parent element.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class X(QuantityT):
    """The X component of a vector or a position.

    The value is a Quantity carrying a unit definition.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Y(QuantityT):
    """The Y component of a vector or a position.

    The value is a Quantity carrying a unit definition.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class YieldStress(QuantityT):
    """
    The material yield stress.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class YoungsModulus(QuantityT):
    """
    The material elasticity modulus.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Z(QuantityT):
    """The Z component of a vector or a position.

    The value is a Quantity carrying a unit definition.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ZposDeckline(QuantityT):
    """
    Vertical distance from baseline to deck-line at FE.
    """
    class Meta:
        name = "ZPosDeckline"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ZposOfDeck(QuantityT):
    """
    Z coordinate of the bulkhead deck.
    """
    class Meta:
        name = "ZPosOfDeck"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class AmountOfSubstance(AmountOfSubstanceType):
    """
    Element containing the dimension of the quantity amount of substance.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class ElectricCurrent(ElectricCurrentType):
    """
    Element containing the dimension of the quantity electric current.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class EnumeratedRootUnitType:
    """Type for the element for a root unit (from an extensive enumerated list)
    allowing an optional prefix and power.

    E.g., mm^2

    Attributes
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
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    unit: Optional[EnumeratedRootUnitTypeUnit] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    source_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceURL",
            "type": "Attribute",
        }
    )
    prefix: Optional[EnumeratedRootUnitTypePrefix] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    power_numerator: int = field(
        default=1,
        metadata={
            "name": "powerNumerator",
            "type": "Attribute",
        }
    )


@dataclass
class Length1(LengthType):
    """
    Element containing the dimension of the quantity length.
    """
    class Meta:
        name = "Length"
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class LuminousIntensity(LuminousIntensityType):
    """
    Element containing the dimension of the quantity luminous intensity.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class Mass(MassType):
    """
    Element containing the dimension of the quantity mass.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class NameType:
    """Type for name.

    Used for names in units, quantities, and prefixes.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ThermodynamicTemperature(ThermodynamicTemperatureType):
    """
    Element containing the dimension of the quantity thermodynamic temerature.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class Time(TimeType):
    """
    Element containing the dimension of the quantity time.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class UnitSymbol(SymbolType):
    """Element containing various unit symbols.

    Examples include Aring (ASCII), Å (HTML).
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class ApplicationRef(ApplicationRefT):
    """
    The ApplicationRef element is meant to relate the parent element (Product,
    Representation, etc) back to the owning entity in the sending application.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BracketRef(BracketRefT):
    """
    A OcxItemPtr reference to a Bracket instance.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulbFlatT:
    """
    BulbFlat type.

    Attributes
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_width: Optional[FlangeWidth] = field(
        default=None,
        metadata={
            "name": "FlangeWidth",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    bulb_angle: Optional[BulbAngle] = field(
        default=None,
        metadata={
            "name": "BulbAngle",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulb_outer_radius: Optional[BulbOuterRadius] = field(
        default=None,
        metadata={
            "name": "BulbOuterRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulb_inner_radius: Optional[BulbInnerRadius] = field(
        default=None,
        metadata={
            "name": "BulbInnerRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulb_top_radius: Optional[BulbTopRadius] = field(
        default=None,
        metadata={
            "name": "BulbTopRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulb_bottom_radius: Optional[BulbBottomRadius] = field(
        default=None,
        metadata={
            "name": "BulbBottomRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class BulkCargoT:
    """
    Type definition of dry cargo properties, reference is made to ISO
    10303-215:2004.
    """
    class Meta:
        name = "BulkCargo_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    stowage_factor: Optional[StowageFactor] = field(
        default=None,
        metadata={
            "name": "StowageFactor",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    permeability: Optional[Permeability] = field(
        default=None,
        metadata={
            "name": "Permeability",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    angle_of_repose: Optional[AngleOfRepose] = field(
        default=None,
        metadata={
            "name": "AngleOfRepose",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulk_cargo_type: Optional[BulkCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "bulkCargoType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ChildRef(ChildRefT):
    """The reference to zero or more child instances.

    A leaf instance does not have any children.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ConnectedBracketRefT(BracketRefT):
    """
    Type definition of a connected bracket part of a ConnectionConfiguration.
    """
    class Meta:
        name = "ConnectedBracketRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    position: Optional[PositionValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class DocumentBaseT:
    """
    Type definition of the abstract base class for the XML document defined in this
    schema.

    Attributes
        header:
        schema_version: Current XML schema version (Format - x.y.z) x :
            Incremented for backward incompatible changes ( Ex - Adding
            a required attribute, etc.) y : Major backward compatible
            changes [ Ex - Adding a new node ,fixing major CRs,etc..] z
            : Minor backward compatible changes (Ex - adding an optional
            attribute, etc).
        language: Language used by the application.
    """
    class Meta:
        name = "DocumentBase_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    header: Optional[Header] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    schema_version: str = field(
        init=False,
        default="2.8.6",
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    language: str = field(
        default="en",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EdgeCurveRef(EdgeCurveRefT):
    """A reference to a Panel, Plate or bracket boundary curve.

    Used as landing curve for a face plate or edge reinforcement
    stiffener.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class EndCutRef(EndCutRefT):
    """
    A reference to the Stiffener end cut detail.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    cutback_distance: Optional[CutbackDistance] = field(
        default=None,
        metadata={
            "name": "CutbackDistance",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EntityBaseT(DescriptionBaseT):
    """
    Abstract base for all structural parts (Panel, Plate, Seam ...) information are
    derived.

    Attributes
        guidref: A globally Unique ID referring an entity in the sending
            application.
    """
    class Meta:
        name = "EntityBase_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class ExternalGeometryRef(ExternalGeometryRefT):
    """
    The ExternalGeometryRef element is used to point to an external geometry
    representation of the parent entity (e.g. Plate, Stiffener, Bracket, Member).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FeatureCopeT:
    """
    Cope parameters.
    """
    class Meta:
        name = "FeatureCope_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    cope_height: Optional[CopeHeight] = field(
        default=None,
        metadata={
            "name": "CopeHeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    cope_radius: Optional[CopeRadius] = field(
        default=None,
        metadata={
            "name": "CopeRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    cope_length: Optional[CopeLength] = field(
        default=None,
        metadata={
            "name": "CopeLength",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class FlangeEdgeReinforcementT:
    """
    Attributes
        flange_width: The width of the bracket flange edge
            reinforcement.
        radius: The bend radius of the transition zone between bracket
            web and bracket flange.
    """
    class Meta:
        name = "FlangeEdgeReinforcement_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    flange_width: Optional[FlangeWidth] = field(
        default=None,
        metadata={
            "name": "FlangeWidth",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class FlatBarT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
    """
    class Meta:
        name = "FlatBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class GaseousCargoT:
    """
    Type definition of  Liquid cargo physical properties.

    Attributes
        density: The density specifies the  of  cargo density.
        carriage_pressure:
        liquid_state: Set to True if the gaseous cargo is carried in a
            liquid state.
        liquid_cargo_type: The liquid cargo types after ISO
            10303-215:2004.
    """
    class Meta:
        name = "GaseousCargo_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    density: Optional[Density] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    carriage_pressure: Optional[CarriagePressure] = field(
        default=None,
        metadata={
            "name": "CarriagePressure",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    liquid_state: bool = field(
        default=False,
        metadata={
            "name": "liquidState",
            "type": "Attribute",
        }
    )
    liquid_cargo_type: Optional[LiquidCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "liquidCargoType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class GeometryRepresentationT(DescriptionBaseT):
    """
    Type definition of the abstract base class for all structural geometry
    definitions.
    """
    class Meta:
        name = "GeometryRepresentation_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class GridSpacingSystemT(DescriptionBaseT):
    """
    The type definition of the grid system.

    Attributes
        grid_position: The location of the first grid position in the
            spacing group.
        spacing:
        first_grid_number: The first grid number in this group
        count: Number of repeated grid spacings
    """
    class Meta:
        name = "GridSpacingSystem_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    grid_position: List[GridPosition] = field(
        default_factory=list,
        metadata={
            "name": "GridPosition",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    spacing: List[Spacing] = field(
        default_factory=list,
        metadata={
            "name": "Spacing",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    first_grid_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "firstGridNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HalfRoundBarT:
    """
    Attributes
        height: Profile height measured along the chord. For a half
            circle it is the diameter.
        width: Profile width measured as the height of the arc from the
            chord. For a half circle it is the radius.
    """
    class Meta:
        name = "HalfRoundBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class HexagonBarT:
    """
    Attributes
        height: The profile height.
    """
    class Meta:
        name = "HexagonBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Hole2DT(DescriptionBaseT):
    """
    Type definition for a 2D hole shape defined either by a parametric hole or a
    curve contour.
    """
    class Meta:
        name = "Hole2D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class HoleRef(HoleRefT):
    """
    A reference to a catalogue 2D hole.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class IbarT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """
    class Meta:
        name = "IBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class LbarOfT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness: Thickness of the web.
        flange_thickness: Thickness of the flange.
        overshoot:
    """
    class Meta:
        name = "LBarOF_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[QuantityT] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    overshoot: Optional[Overshoot] = field(
        default=None,
        metadata={
            "name": "Overshoot",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class LbarOwT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
        overshoot: Overshoot of the web above the flange. Should be
            added to the Height to get the total height.
    """
    class Meta:
        name = "LBarOW_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    overshoot: Optional[Overshoot] = field(
        default=None,
        metadata={
            "name": "Overshoot",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class LbarT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """
    class Meta:
        name = "LBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class LiquidCargoT:
    """
    Type definition of  Liquid cargo physical properties.

    Attributes
        density: The density of  ballast, bunker or liquid cargo
            content.
        carriage_pressure:
        liquid_cargo_type:
    """
    class Meta:
        name = "LiquidCargo_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    density: Optional[Density] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    carriage_pressure: Optional[CarriagePressure] = field(
        default=None,
        metadata={
            "name": "CarriagePressure",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    liquid_cargo_type: Optional[LiquidCargoTypeValue] = field(
        default=None,
        metadata={
            "name": "liquidCargoType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class LugPlateRefT(EntityRefBaseT):
    """
    Plate lug reference type with lug parameters.

    Attributes
        connection_length: Length of lug plate connection welded to
            stiffener web.
        distance_above:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "LugPlateRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    connection_length: Optional[ConnectionLength] = field(
        default=None,
        metadata={
            "name": "ConnectionLength",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    distance_above: Optional[DistanceAbove] = field(
        default=None,
        metadata={
            "name": "DistanceAbove",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PLATE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class MaterialRef(MaterialRefT):
    """
    A reference to the parent's material.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MaterialT(DescriptionBaseT):
    """
    Type definition of a Material with physical properties.
    """
    class Meta:
        name = "Material_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    density: List[Density] = field(
        default_factory=list,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    youngs_modulus: List[YoungsModulus] = field(
        default_factory=list,
        metadata={
            "name": "YoungsModulus",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poisson_ratio: List[PoissonRatio] = field(
        default_factory=list,
        metadata={
            "name": "PoissonRatio",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    yield_stress: List[YieldStress] = field(
        default_factory=list,
        metadata={
            "name": "YieldStress",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ultimate_stress: List[UltimateStress] = field(
        default_factory=list,
        metadata={
            "name": "UltimateStress",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    thermal_expansion_coefficient: List[ThermalExpansionCoefficient] = field(
        default_factory=list,
        metadata={
            "name": "ThermalExpansionCoefficient",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    grade: Optional[GradeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class Nurbsproperties(NurbspropertiesT):
    """
    Properties of the basis functions in surface V direction.
    """
    class Meta:
        name = "NURBSproperties"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OctagonBarT:
    """
    Attributes
        height: Profile height and width measured as the distance
            between two parallel sides.
    """
    class Meta:
        name = "OctagonBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class ParametricHole2DT(DescriptionBaseT):
    """
    Type definition of a set of parametric hole definitions.
    """
    class Meta:
        name = "ParametricHole2D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PlateMaterialT(MaterialRefT):
    """
    Type definition the Plate material and plate thickenss.
    """
    class Meta:
        name = "PlateMaterial_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Point3DT:
    """
    Type definition of a point in 3D space composed of X, Y and Z coordinate
    values.

    Attributes
        x: The X component of the origin position. The value is a
            Quantity carrying a unit definition.
        y: The Y component of the origin position. The value is a
            Quantity carrying a unit definition.
        z: The Z component of the origin position. The value is a
            Quantity carrying a unit definition.
    """
    class Meta:
        name = "Point3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    x: Optional[X] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    y: Optional[Y] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    z: Optional[Z] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class PrincipalParticularsT:
    """
    Type definition of the  main vessel particulars required by the Society.

    Attributes
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
            Rules. Type 'A' ship is one which: — is designed to carry
            only liquid cargoes in bulk — has a high integrity of the
            exposed deck with only small access openings to cargo
            compartments, closed by watertight gasket covers of steel or
            equivalent material — has low permeability of loaded cargo
            compartments. All ships which are not Type 'A' ships shall
            be considered as Type 'B' ships.
            .
        number_of_decks_above: Number of decks above 0.7 D from
            baseline.
    """
    class Meta:
        name = "PrincipalParticulars_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    lpp: List[Lpp] = field(
        default_factory=list,
        metadata={
            "name": "Lpp",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    rule_length: List[RuleLength] = field(
        default_factory=list,
        metadata={
            "name": "RuleLength",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    block_coefficient: List[BlockCoefficient] = field(
        default_factory=list,
        metadata={
            "name": "BlockCoefficient",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    fp_pos: List[FpPos] = field(
        default_factory=list,
        metadata={
            "name": "FP_Pos",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    moulded_breadth: List[MouldedBreadth] = field(
        default_factory=list,
        metadata={
            "name": "MouldedBreadth",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    moulded_depth: List[MouldedDepth] = field(
        default_factory=list,
        metadata={
            "name": "MouldedDepth",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    scantling_draught: List[ScantlingDraught] = field(
        default_factory=list,
        metadata={
            "name": "ScantlingDraught",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    design_speed: List[DesignSpeed] = field(
        default_factory=list,
        metadata={
            "name": "DesignSpeed",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    freeboard_length: List[FreeboardLength] = field(
        default_factory=list,
        metadata={
            "name": "FreeboardLength",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    normal_ballast_draught: List[NormalBallastDraught] = field(
        default_factory=list,
        metadata={
            "name": "NormalBallastDraught",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    heavy_ballast_draught: List[HeavyBallastDraught] = field(
        default_factory=list,
        metadata={
            "name": "HeavyBallastDraught",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    slamming_draught_empty_fp: List[SlammingDraughtEmptyFp] = field(
        default_factory=list,
        metadata={
            "name": "SlammingDraughtEmptyFP",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    slamming_draught_full_fp: List[SlammingDraughtFullFp] = field(
        default_factory=list,
        metadata={
            "name": "SlammingDraughtFullFP",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    length_of_waterline: List[LengthOfWaterline] = field(
        default_factory=list,
        metadata={
            "name": "LengthOfWaterline",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    freeboard_deck_height: List[FreeboardDeckHeight] = field(
        default_factory=list,
        metadata={
            "name": "FreeboardDeckHeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ap_pos: List[ApPos] = field(
        default_factory=list,
        metadata={
            "name": "AP_Pos",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    zpos_of_deck: List[ZposOfDeck] = field(
        default_factory=list,
        metadata={
            "name": "ZPosOfDeck",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    deepest_equilibrium_wl: List[DeepestEquilibriumWl] = field(
        default_factory=list,
        metadata={
            "name": "DeepestEquilibriumWL",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    upper_deck_area: List[UpperDeckArea] = field(
        default_factory=list,
        metadata={
            "name": "UpperDeckArea",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    water_plane_area: List[WaterPlaneArea] = field(
        default_factory=list,
        metadata={
            "name": "WaterPlaneArea",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    zpos_deckline: List[ZposDeckline] = field(
        default_factory=list,
        metadata={
            "name": "ZPosDeckline",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    speed_factor: List[SpeedFactor] = field(
        default_factory=list,
        metadata={
            "name": "SpeedFactor",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    has_deadweight_less_than: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasDeadweightLessThan",
            "type": "Attribute",
        }
    )
    has_bilge_keel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasBilgeKeel",
            "type": "Attribute",
        }
    )
    freeboard_type: FreeboardTypeValue = field(
        default=FreeboardTypeValue.A,
        metadata={
            "name": "freeboardType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    number_of_decks_above: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfDecksAbove",
            "type": "Attribute",
        }
    )


@dataclass
class ProcessLayerT(DescriptionBaseT):
    """
    Type definition for the ProcessLayer.
    """
    class Meta:
        name = "ProcessLayer_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RectangularTube(RectangularTubeT):
    """
    Rectangular tube.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RootRef(RootRefT):
    """
    RootRef is an OcXItemPtr pointing to the top-level instance in a ProductView.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RoundBarT:
    """
    Attributes
        height: Profile diameter.
    """
    class Meta:
        name = "RoundBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SchemaChangeT:
    """
    Used to embed documentation of schema changes directly in the schema.

    Attributes
        description: A description of the change. Each SchemaChange
            should contain exactly one Description sub-element.
        reference:
        author: The author of the change.
        date: The date on which the change took effect.
        version: The version number of the schema that the change
            applies to.
    """
    class Meta:
        name = "SchemaChange_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SectionPropertiesT:
    """
    Generic bar section properties.

    Attributes
        area: Cross-section area.
        neutral_axis_u:
        neutral_axis_v:
        inertia_u:
        inertia_v:
        torsion_constant:
    """
    class Meta:
        name = "SectionProperties_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    area: Optional[Area] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    neutral_axis_u: Optional[NeutralAxisU] = field(
        default=None,
        metadata={
            "name": "NeutralAxisU",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    neutral_axis_v: Optional[NeutralAxisV] = field(
        default=None,
        metadata={
            "name": "NeutralAxisV",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    inertia_u: Optional[InertiaU] = field(
        default=None,
        metadata={
            "name": "InertiaU",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    inertia_v: Optional[InertiaV] = field(
        default=None,
        metadata={
            "name": "InertiaV",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    torsion_constant: Optional[TorsionConstant] = field(
        default=None,
        metadata={
            "name": "TorsionConstant",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class SectionRef(SectionRefT):
    """
    A reference to the parent's cross section.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    offset_u: Optional[OffsetU] = field(
        default=None,
        metadata={
            "name": "OffsetU",
            "type": "Element",
        }
    )
    offset_v: Optional[OffsetV] = field(
        default=None,
        metadata={
            "name": "OffsetV",
            "type": "Element",
        }
    )


@dataclass
class SquareBarT:
    """
    Attributes
        height: Profile height, measured along the web.
    """
    class Meta:
        name = "SquareBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SweepT:
    """
    Type definition of a sweep extent defined by a direction and length.

    Attributes
        vector3_d: The sweep direction given by a Unit vector of length
            1.
        length: The extent of the sweep.
    """
    class Meta:
        name = "Sweep_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    vector3_d: Optional[Vector3D] = field(
        default=None,
        metadata={
            "name": "Vector3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    length: Optional[Length2] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class TbarT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """
    class Meta:
        name = "TBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class TonnageDataT:
    """
    The information pertinent to the tonnage of the ship.
    """
    class Meta:
        name = "TonnageData_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    tonnage: Optional[Tonnage] = field(
        default=None,
        metadata={
            "name": "Tonnage",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    dead_weight: Optional[DeadWeight] = field(
        default=None,
        metadata={
            "name": "DeadWeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class TubeT:
    """
    Attributes
        diameter: The tube diameter.
        thickness:
    """
    class Meta:
        name = "Tube_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    diameter: Optional[Diameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    thickness: Optional[Thickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class UbarT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """
    class Meta:
        name = "UBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class UNurbsproperties(NurbspropertiesT):
    """
    Properties of the basis functions in surface U direction.
    """
    class Meta:
        name = "U_NURBSproperties"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UnitCargo(UnitCargoT):
    """The UnitCargo type is intended for spaces carrying a type of dry cargo that
    that is packed or comprises discrete units that can be loaded and stored
    individually on the ship.

    Ref. is made to ISO 10303-215:2004.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UserDefinedParameter(UserDefinedParameterT):
    """
    A user-defined parameter which can be provided to define a user-defined
    BarSection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class VNurbsproperties(NurbspropertiesT):
    """
    Properties of the basis functions in surface V direction.
    """
    class Meta:
        name = "V_NURBSproperties"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ZbarT:
    """
    Attributes
        height: Profile height, measured along the web.
        width: Profile width and web thickness.
        web_thickness:
        flange_thickness:
    """
    class Meta:
        name = "ZBar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_thickness: Optional[WebThickness] = field(
        default=None,
        metadata={
            "name": "WebThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_thickness: Optional[FlangeThickness] = field(
        default=None,
        metadata={
            "name": "FlangeThickness",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class DimensionType:
    """
    Type for dimension.

    Attributes
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
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    length: List[Length1] = field(
        default_factory=list,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    mass: List[Mass] = field(
        default_factory=list,
        metadata={
            "name": "Mass",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    time: List[Time] = field(
        default_factory=list,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    electric_current: List[ElectricCurrent] = field(
        default_factory=list,
        metadata={
            "name": "ElectricCurrent",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    thermodynamic_temperature: List[ThermodynamicTemperature] = field(
        default_factory=list,
        metadata={
            "name": "ThermodynamicTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    amount_of_substance: List[AmountOfSubstance] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfSubstance",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    luminous_intensity: List[LuminousIntensity] = field(
        default_factory=list,
        metadata={
            "name": "LuminousIntensity",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "sequence": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )
    dimensionless: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EnumeratedRootUnit(EnumeratedRootUnitType):
    """Element for a root unit (from an extensive enumerated list) allowing an
    optional prefix and power.

    E.g., mm^2
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class UnitName(NameType):
    """
    Element containing the unit name.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class BulbFlat(BulbFlatT):
    """
    Bulb bar, rolled or welded.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BulkCargo(BulkCargoT):
    """A bulk cargo is a type of dry cargo that is solid cargo that is not packed,
    but is carried loose.

    Ref. is made to ISO 10303-215:2004.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Center(Point3DT):
    """
    The center position of a shape.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CenterOfGravity(Point3DT):
    """The center of gravity (COG) of the parent object.

    The receiving application can use the value received from the
    authoring application to check that the object has been transferred
    correctly.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ConnectedBracketRef(ConnectedBracketRefT):
    """
    The reference to a connected bracket part of a ConnectionConfiguration.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Curve3DT(GeometryRepresentationT):
    """
    Type definition of the abstract base class for any 3D curve.

    Attributes
        length:
        is2_d: Set to True if the Curve3D is given in 2D space.
    """
    class Meta:
        name = "Curve3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    length: Optional[Length2] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    is2_d: bool = field(
        default=False,
        metadata={
            "name": "is2D",
            "type": "Attribute",
        }
    )


@dataclass
class EndPoint(Point3DT):
    """
    The end position of the segment.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FeatureCope(FeatureCopeT):
    """
    Parameters of cope features defining additional bracket or stiffener end cut
    details.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlangeEdgeReinforcement(FlangeEdgeReinforcementT):
    """
    Bracket flange edge reinforcement parameters.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FlatBar(FlatBarT):
    """
    Flat bar, rolled or cut from plate.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FormT(EntityBaseT):
    """
    Abstract base type  definition of the Form element.
    """
    class Meta:
        name = "Form_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    distance_tolerance: Optional[DistanceTolerance] = field(
        default=None,
        metadata={
            "name": "DistanceTolerance",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    angle_tolerance: Optional[AngleTolerance] = field(
        default=None,
        metadata={
            "name": "AngleTolerance",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class GaseousCargo(GaseousCargoT):
    """Liquid cargo properties, reference is made to ISO 10303-215:2004.

    A Gaseous cargo is a type of Cargo that has a natural condition of a
    non-solid, nonliquid gaseous state.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class HalfRoundBar(HalfRoundBarT):
    """
    Half round bar.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class HexagonBar(HexagonBarT):
    """
    A symmetrical hexagon shaped bar.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Ibar(IbarT):
    """
    I-section bar, rolled or welded.
    """
    class Meta:
        name = "IBar"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class IntermediatePoint(Point3DT):
    """
    An intermediate point on the circular segment.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Lbar(LbarT):
    """
    An angle bar, rolled or welded.
    """
    class Meta:
        name = "LBar"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LbarOf(LbarOfT):
    """
    Welded angle bar where the flange has an overshoot beyond the web.
    """
    class Meta:
        name = "LBarOF"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LbarOw(LbarOwT):
    """
    Welded angle bar where the web has an overshoot above the flange.
    """
    class Meta:
        name = "LBarOW"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LiquidCargo(LiquidCargoT):
    """Liquid cargo properties, reference is made to ISO 10303-215:2004.

    A liquid cargo is a type of Cargo whose natural condition is a non-
    solid, non-gaseous liquid state.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LugPlateRef(LugPlateRefT):
    """
    The reference to plate lugs with additional lug parameters.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Material(MaterialT):
    """
    Physical properties of a material.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Max(Point3DT):
    """
    The max position of the bounding box diagonal.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Min(Point3DT):
    """
    The min position of the bounding box diagonal.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OccurrenceT(EntityRefBaseT):
    """
    The type definition for the Occurrence reference.

    Attributes
        child_ref:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "Occurrence_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    child_ref: List[ChildRef] = field(
        default_factory=list,
        metadata={
            "name": "ChildRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ref_type: Optional[RefTypeValue] = field(
        default=None,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class OctagonBar(OctagonBarT):
    """
    An octagon shaped bar.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Origin(Point3DT):
    """
    The origin of a local or global coordinate system.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ParametricCircleT(ParametricHole2DT):
    """
    Type definition of the  parametric circle in u-v space defined by a diameter.
    """
    class Meta:
        name = "ParametricCircle_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    diameter: Optional[Diameter] = field(
        default=None,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class PlateMaterial(PlateMaterialT):
    """
    Definition of the Plate material and plate thickenss.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Point3D(Point3DT):
    """
    A point in 3D space composed of X, Y and Z coordinate values.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Position(Point3DT):
    """
    The position of the inclination of the cross section.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PrincipalParticulars(PrincipalParticularsT):
    """
    Main vessel particulars required by the Society.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RadialCylinderT(EntityBaseT):
    """
    Cylindrical reference system.
    """
    class Meta:
        name = "RadialCylinder_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class RectangularHoleT(ParametricHole2DT):
    """
    Type definition of  a rectangular hole with corner fillet radii.

    Attributes
        height: The height of the hole.
        width: The width of the hole.
        fillet_radius: Corner fillet radius. If not given, the fillet
            radius is taken as 0.5*Min of (Height,Width), i.e. half of
            the smallest of the Height or the Width .
    """
    class Meta:
        name = "RectangularHole_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    fillet_radius: Optional[FilletRadius] = field(
        default=None,
        metadata={
            "name": "FilletRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class RectangularMickeyMouseEarsT(ParametricHole2DT):
    """
    A hole where the two circular parts have unequal radii.

    Attributes
        height: The height of the hole.
        width: The width of the hole.
        radius: The radius of the Mickey Mouse ear.
        displacement:
    """
    class Meta:
        name = "RectangularMickeyMouseEars_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    displacement: Optional[Displacement] = field(
        default=None,
        metadata={
            "name": "Displacement",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class RefPlaneT(EntityBaseT):
    """
    Type definition of a reference plane used to define unbounded planar geometry.
    """
    class Meta:
        name = "RefPlane_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RoundBar(RoundBarT):
    """
    Round bar.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SchemaChange(SchemaChangeT):
    """
    Element holding embedded schema changes recording the history of schema
    versions.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SectionProperties(SectionPropertiesT):
    """
    Generic bar section properties.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SquareBar(SquareBarT):
    """
    Square bar.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StartPoint(Point3DT):
    """
    The start position of the segment.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SuperEllipticalT(ParametricHole2DT):
    """Type definition of a super-elliptical hole.

    It can also describe a true ellipse.

    Attributes
        height:
        width:
        exponent: The exponent of the "super ellipse" equation
            (x/Height)**e + (y/Width)**e = 1. If e=2.5 the result is a
            super ellipse while e=2.0 results in a normal ellipse.
    """
    class Meta:
        name = "SuperElliptical_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    exponent: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Sweep(SweepT):
    """
    Defeintion of the sweep extent  by a direction and sweep  length.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SymmetricalHoleT(ParametricHole2DT):
    """
    Type definition of a hole made of two semi-circles connected by two straight
    lines.

    Attributes
        height: The height of the hole.
        width: The width of the hole.
    """
    class Meta:
        name = "SymmetricalHole_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Tbar(TbarT):
    """
    T-section bar, rolled or welded.
    """
    class Meta:
        name = "TBar"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Tip(Point3DT):
    """
    Cone tip position.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class TonnageData(TonnageDataT):
    """
    The Vessel tonnage information.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Tube(TubeT):
    """
    Circular tube.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Ubar(UbarT):
    """
    U-section bar, rolled or welded.
    """
    class Meta:
        name = "UBar"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class XspacingGroup(GridSpacingSystemT):
    """
    The definition of a frame spacing group for a sequence of frame positions with
    equal spacing.
    """
    class Meta:
        name = "XSpacingGroup"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class YspacingGroup(GridSpacingSystemT):
    """
    The definition of a grid spacing group for a sequence of grid positions with
    equal spacing.
    """
    class Meta:
        name = "YSpacingGroup"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Zbar(ZbarT):
    """
    Z-section bar, rolled or welded.
    """
    class Meta:
        name = "ZBar"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ZspacingGroup(GridSpacingSystemT):
    """
    The definition of a grid spacing group for a sequence of grid positions with
    equal spacing.
    """
    class Meta:
        name = "ZSpacingGroup"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Dimension(DimensionType):
    """
    Element to express the dimension of a unit or quantity in terms of the SI base
    quantities length, mass, time, electric current, thermodynamic temperature,
    amount of substance, and luminous intensity.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class RootUnitsType:
    """Type for the container for defining derived units in terms of their root
    units.

    This allows a precise definition of a wide range of units. The goal
    is to improve interoperability among applications and databases
    which use derived units based on commonly encountered base units.

    Attributes
        enumerated_root_unit: Element for a root unit (from an extensive
            enumerated list) allowing an optional prefix and power.
            E.g., mm^2
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    enumerated_root_unit: List[EnumeratedRootUnit] = field(
        default_factory=list,
        metadata={
            "name": "EnumeratedRootUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )


@dataclass
class BoundingBoxT:
    class Meta:
        name = "BoundingBox_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    max: List[Max] = field(
        default_factory=list,
        metadata={
            "name": "Max",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 2,
        }
    )
    min: List[Min] = field(
        default_factory=list,
        metadata={
            "name": "Min",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 2,
        }
    )


@dataclass
class BracketParametersT:
    """
    Type definition of Common parameters defining bracket configurations used in
    shipbuilding.

    Attributes
        arm_length_u:
        arm_length_v:
        udirection: Local U deirection of the Bracket
        vdirection: Local V direction of the Bracket.
        origin: The origin or root point of the Bracket
        unose:
        vnose:
        free_edge_radius:
        feature_cope:
        flange_edge_reinforcement:
        has_edge_reinforcement:
        number_of_supports: Number of supported (welded) bracket edges.
        edge_reinforcement:
    """
    class Meta:
        name = "BracketParameters_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    arm_length_u: Optional[ArmLengthU] = field(
        default=None,
        metadata={
            "name": "ArmLengthU",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    arm_length_v: Optional[ArmLengthV] = field(
        default=None,
        metadata={
            "name": "ArmLengthV",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    udirection: Optional[Udirection] = field(
        default=None,
        metadata={
            "name": "UDirection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    vdirection: Optional[Vdirection] = field(
        default=None,
        metadata={
            "name": "VDirection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    unose: Optional[Unose] = field(
        default=None,
        metadata={
            "name": "Unose",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    vnose: Optional[Vnose] = field(
        default=None,
        metadata={
            "name": "Vnose",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    free_edge_radius: Optional[FreeEdgeRadius] = field(
        default=None,
        metadata={
            "name": "FreeEdgeRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    feature_cope: Optional[FeatureCope] = field(
        default=None,
        metadata={
            "name": "FeatureCope",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    flange_edge_reinforcement: Optional[FlangeEdgeReinforcement] = field(
        default=None,
        metadata={
            "name": "FlangeEdgeReinforcement",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    has_edge_reinforcement: bool = field(
        default=False,
        metadata={
            "name": "hasEdgeReinforcement",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    number_of_supports: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSupports",
            "type": "Attribute",
        }
    )
    edge_reinforcement: Optional[EdgeReinforcementValue] = field(
        default=None,
        metadata={
            "name": "edgeReinforcement",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Circle3DT(Curve3DT):
    """
    Type definition of a circle in 3D space.

    Attributes
        diameter: The circle diameter.
        center: The center of the circle.
        normal: The normal vector of the    the circle plane.
    """
    class Meta:
        name = "Circle3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    diameter: List[Diameter] = field(
        default_factory=list,
        metadata={
            "name": "Diameter",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 3,
        }
    )
    center: List[Center] = field(
        default_factory=list,
        metadata={
            "name": "Center",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 3,
        }
    )
    normal: List[Normal] = field(
        default_factory=list,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 3,
        }
    )


@dataclass
class CircumArc3DT(Curve3DT):
    """
    Type definition of a 3D Line/Arc representation defined by thee points in 3D
    space.
    """
    class Meta:
        name = "CircumArc3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    start_point: Optional[StartPoint] = field(
        default=None,
        metadata={
            "name": "StartPoint",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    intermediate_point: Optional[IntermediatePoint] = field(
        default=None,
        metadata={
            "name": "IntermediatePoint",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    end_point: Optional[EndPoint] = field(
        default=None,
        metadata={
            "name": "EndPoint",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class ClassDataT:
    """
    Type definition of the main vessel data including Class Notation required by
    the Classification Society.

    Attributes
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
            when @newbuildingSociety = 'OTHER' .
        society:
        society_name: The common name of the class society relevant for
            operating the ship. Needs only to be specified when @society
            = 'OTHER'                          .
    """
    class Meta:
        name = "ClassData_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    principal_particulars: Optional[PrincipalParticulars] = field(
        default=None,
        metadata={
            "name": "PrincipalParticulars",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    class_notation: Optional[ClassNotation] = field(
        default=None,
        metadata={
            "name": "ClassNotation",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    newbuilding_society: Optional[ClassificationSociety] = field(
        default=None,
        metadata={
            "name": "newbuildingSociety",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    identification: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    newbuilding_society_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "newbuildingSocietyName",
            "type": "Attribute",
        }
    )
    society: Optional[ClassificationSociety] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    society_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "societyName",
            "type": "Attribute",
        }
    )


@dataclass
class CompartmentPropertiesT:
    """
    Type definition of the physical properties of a compartment volume (COG, air
    pipe top).

    Attributes
        center_of_gravity: COG of the closed space.
        volume:
        air_pipe_height:
        filling_height: The filling height specifies the maximum height
            for filling of the tank compartment.
        relief_valve_pressure:
    """
    class Meta:
        name = "CompartmentProperties_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    center_of_gravity: Optional[CenterOfGravity] = field(
        default=None,
        metadata={
            "name": "CenterOfGravity",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    volume: Optional[Volume] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    air_pipe_height: Optional[AirPipeHeight] = field(
        default=None,
        metadata={
            "name": "AirPipeHeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    filling_height: Optional[FillingHeight] = field(
        default=None,
        metadata={
            "name": "FillingHeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    relief_valve_pressure: Optional[ReliefValvePressure] = field(
        default=None,
        metadata={
            "name": "ReliefValvePressure",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ControlPointT:
    """
    Type definition of the NURBS control point.

    Attributes
        point3_d:
        weight: The weight associated with the control point. The weight
            is 1.0 if not given (default).
    """
    class Meta:
        name = "ControlPoint_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    point3_d: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    weight: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DoubleBracketT:
    """
    Type definition of DoubleBracket connection.

    Attributes
        connected_bracket_ref: The reference to a connected bracket part
            of a ConnectionConfiguration. For a double bracket
            connection type, two references must be provided.
    """
    class Meta:
        name = "DoubleBracket_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    connected_bracket_ref: List[ConnectedBracketRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )


@dataclass
class Ellipse3DT(Curve3DT):
    """
    Type definition of An ellipse in 3D space.

    Attributes
        center: The center of the ellipse.
        major_diameter:
        minor_diameter:
        major_axis:
        minor_axis:
        normal:
    """
    class Meta:
        name = "Ellipse3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    center: Optional[Center] = field(
        default=None,
        metadata={
            "name": "Center",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    major_diameter: Optional[MajorDiameter] = field(
        default=None,
        metadata={
            "name": "MajorDiameter",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    minor_diameter: Optional[MinorDiameter] = field(
        default=None,
        metadata={
            "name": "MinorDiameter",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    major_axis: Optional[MajorAxis] = field(
        default=None,
        metadata={
            "name": "MajorAxis",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    minor_axis: Optional[MinorAxis] = field(
        default=None,
        metadata={
            "name": "MinorAxis",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    normal: Optional[Normal] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class EndCutT(DescriptionBaseT):
    """
    Type definition of stiffener end cut parameters.

    Attributes
        section_ref:
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    cutback_distance: Optional[CutbackDistance] = field(
        default=None,
        metadata={
            "name": "CutbackDistance",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    web_cut_back_angle: Optional[WebCutBackAngle] = field(
        default=None,
        metadata={
            "name": "WebCutBackAngle",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    web_nose_height: Optional[WebNoseHeight] = field(
        default=None,
        metadata={
            "name": "WebNoseHeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    flange_cut_back_angle: Optional[FlangeCutBackAngle] = field(
        default=None,
        metadata={
            "name": "FlangeCutBackAngle",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    flange_nose_height: Optional[FlangeNoseHeight] = field(
        default=None,
        metadata={
            "name": "FlangeNoseHeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    feature_cope: Optional[FeatureCope] = field(
        default=None,
        metadata={
            "name": "FeatureCope",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    symmetric_flange: bool = field(
        default=False,
        metadata={
            "name": "symmetricFlange",
            "type": "Attribute",
        }
    )
    sniped: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EquipmentT(FormT):
    """
    Type definition of the Equipment element.
    """
    class Meta:
        name = "Equipment_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class InclinationT:
    """
    Type definition of inclination of stiffener or member along its trace line (web
    and flange directions)..
    """
    class Meta:
        name = "Inclination_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    web_direction: Optional[WebDirection] = field(
        default=None,
        metadata={
            "name": "WebDirection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    flange_direction: Optional[FlangeDirection] = field(
        default=None,
        metadata={
            "name": "FlangeDirection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    position: Optional[Position] = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Line3DlistT:
    """
    Type definition of a list of straight line segments in 3D space.
    """
    class Meta:
        name = "Line3DList_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    point3_d: List[Point3D] = field(
        default_factory=list,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class Line3DT(Curve3DT):
    """
    Type definition of a straight line defined by two points.
    """
    class Meta:
        name = "Line3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    start_point: Optional[StartPoint] = field(
        default=None,
        metadata={
            "name": "StartPoint",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    end_point: Optional[EndPoint] = field(
        default=None,
        metadata={
            "name": "EndPoint",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class MaterialCatalogueT(DescriptionBaseT):
    """
    Type definition of the material types used and their properties recognised by
    the Society.
    """
    class Meta:
        name = "MaterialCatalogue_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    material: List[Material] = field(
        default_factory=list,
        metadata={
            "name": "Material",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class Occurrence(OccurrenceT):
    """
    The refence to the part's occurrence in a defined view or configuration.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ParametricCircle(ParametricCircleT):
    """
    A parametric circle in u-v space defined by a diameter.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PhysicalPropertiesT:
    """
    Type definition of physical properties of structure objects (weight and centre
    of gravity).
    """
    class Meta:
        name = "PhysicalProperties_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    dry_weight: Optional[DryWeight] = field(
        default=None,
        metadata={
            "name": "DryWeight",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    center_of_gravity: Optional[CenterOfGravity] = field(
        default=None,
        metadata={
            "name": "CenterOfGravity",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Point3DlistT:
    """
    Type definition of a list of positions in 3D space.
    """
    class Meta:
        name = "Point3DList_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    point3_d: List[Point3D] = field(
        default_factory=list,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 2,
        }
    )


@dataclass
class RadialCylinder(RadialCylinderT):
    """
    Cylindrical reference system.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RectangularHole(RectangularHoleT):
    """
    A rectangular hole in u-v space with corner fillets of equal radii.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RectangularMickeyMouseEars(RectangularMickeyMouseEarsT):
    """
    A rectangular hole with corner radii in the form of Mickey Mouse ears.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RefPlane(RefPlaneT):
    """
    A reference plane used to define unbounded planar geometry.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    reference_location: Optional[ReferenceLocation] = field(
        default=None,
        metadata={
            "name": "ReferenceLocation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SingleBracketT:
    """
    Type definition of DoubleBracket connection.
    """
    class Meta:
        name = "SingleBracket_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    connected_bracket_ref: Optional[ConnectedBracketRef] = field(
        default=None,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SlotParametersT:
    """
    Type definition of the SlotParameters for a slot cut-out typically used in
    shipbuilding.

    Attributes
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    width: Optional[Width] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    upper_radius: Optional[UpperRadius] = field(
        default=None,
        metadata={
            "name": "UpperRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    connection_length: Optional[ConnectionLength] = field(
        default=None,
        metadata={
            "name": "ConnectionLength",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    lower_radius: Optional[LowerRadius] = field(
        default=None,
        metadata={
            "name": "LowerRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    lug_plate_ref: List[LugPlateRef] = field(
        default_factory=list,
        metadata={
            "name": "LugPlateRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 2,
        }
    )
    asymmetric: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    slot_type: SlotParametersTSlotType = field(
        default=SlotParametersTSlotType.OPEN,
        metadata={
            "name": "slotType",
            "type": "Attribute",
        }
    )


@dataclass
class SuperElliptical(SuperEllipticalT):
    """A super-elliptical hole.

    It can also describe a true ellipse.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SymmetricalHole(SymmetricalHoleT):
    """
    A hole made of two semi-circles connected by two straight lines.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class TransformationT:
    """
    Type definition for a Local (Orthogonal) Axis System.
    """
    class Meta:
        name = "Transformation_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    primary_axis: Optional[PrimaryAxis] = field(
        default=None,
        metadata={
            "name": "PrimaryAxis",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    secondary_axis: Optional[SecondaryAxis] = field(
        default=None,
        metadata={
            "name": "SecondaryAxis",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class XgridT(DescriptionBaseT):
    """
    Type definition of XGrid definition.

    Attributes
        distance_to_ap:
        xspacing_group:
        is_reversed: true if the frame table is reversed with the origin
            at the fore of the vessel. The defaullt is false.
        is_main_system: True if the FrameTable defines the main vessel
            grid. The default is true.
    """
    class Meta:
        name = "XGrid_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    distance_to_ap: Optional[DistanceToAp] = field(
        default=None,
        metadata={
            "name": "DistanceToAP",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    xspacing_group: List[XspacingGroup] = field(
        default_factory=list,
        metadata={
            "name": "XSpacingGroup",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    is_reversed: bool = field(
        default=False,
        metadata={
            "name": "isReversed",
            "type": "Attribute",
        }
    )
    is_main_system: bool = field(
        default=True,
        metadata={
            "name": "isMainSystem",
            "type": "Attribute",
        }
    )


@dataclass
class YgridT(DescriptionBaseT):
    """
    Type definition of YGrid.
    """
    class Meta:
        name = "YGrid_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    yspacing_group: List[YspacingGroup] = field(
        default_factory=list,
        metadata={
            "name": "YSpacingGroup",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class ZgridT(DescriptionBaseT):
    """
    Type definition of ZGrid.
    """
    class Meta:
        name = "ZGrid_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    zspacing_group: List[ZspacingGroup] = field(
        default_factory=list,
        metadata={
            "name": "ZSpacingGroup",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class DimensionSetType:
    """
    Type for the dimension container.

    Attributes
        dimension: Element to express a unit or quantity in terms of the
            SI base quantities length, mass, time, electric current,
            thermodynamic temperature, amount of substance, and luminous
            intensity.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "min_occurs": 1,
        }
    )


@dataclass
class RootUnits(RootUnitsType):
    """Container for defining derived units in terms of their root units.

    This allows a precise definition of a wide range of units. The goal
    is to improve interoperability among applications and databases
    which use derived units based on commonly encountered root units.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class BoundingBox(BoundingBoxT):
    """
    The definition of a bounding box in space using two positions.The bounding box
    defines the parent extent.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BracketParameters(BracketParametersT):
    """
    Bracket parameters necessary for the verification by the sosciety.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Circle3D(Circle3DT):
    """
    A circle in 3D space.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CircumArc3D(CircumArc3DT):
    """3D Line/Arc representation.

    Represents a semi-circle uniquely defined by three points in 3D
    space given by the start position, intermediate position and the end
    position..
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ClassificationData(ClassDataT):
    """
    Information that specifies design and intended performance characteristics of
    the ship in accordance with classification society rules and statutory
    regulations (see ISO       10303-218, section 4.2.36).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CompartmentProperties(CompartmentPropertiesT):
    """
    The physical properties of a compartment volume (COG, air pipe top).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ControlPoint(ControlPointT):
    """
    A NURBS control point composed of a weight and spatial position.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CylindricalAxesT:
    """
    Cylindrical reference system.
    """
    class Meta:
        name = "CylindricalAxes_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    radial_cylinder: List[RadialCylinder] = field(
        default_factory=list,
        metadata={
            "name": "RadialCylinder",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class DoubleBracket(DoubleBracketT):
    """A double bracket type connection.

    The reference to a connected bracket part of a
    ConnectionConfiguration. For a double bracket connection type, two
    references must be provided.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Ellipse3D(Ellipse3DT):
    """
    An ellipse in 3D space.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class EndCutEnd1(EndCutT):
    """
    The siffener end cut detailing.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class EndCutEnd2(EndCutT):
    """
    Stiffener end cut detailing at end 2.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Equipment(EquipmentT):
    """
    Place holder for future equipment support (To be designed).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Inclination(InclinationT):
    """The inclination of the cross section of a stiffener or a pillar along its
    trace line.

    A vector pair giving the local orientation of the web and flange
    directions at the point given by the Position element. The
    FlangeDirection is optional and not necessary for a symmetrical
    cross section. Only one inclination is necessary for a non-twisted
    (straight) stiffener or pillar.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Line3D(Line3DT):
    """
    A straight line defined by two points.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Line3Dlist(Point3DlistT):
    """
    A list of straight line segments in 3D space.
    """
    class Meta:
        name = "Line3DList"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class LocalCartesian(TransformationT):
    """To specify a Local (Orthogonal) Axis System Origin and two of the local
    X,Y,Z axis need to be specified.

    When used to specify a Plane the XY (UV) plane is considered.
    Optional if the coordinate system is referring to the global
    coordinate frame.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MaterialCatalogue(MaterialCatalogueT):
    """
    The material types used and their properties recognised by the Society.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OccurrenceGroupT(DescriptionBaseT):
    """
    The type definition for the OccurrenceGroup.
    """
    class Meta:
        name = "OccurrenceGroup_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    occurrence: List[Occurrence] = field(
        default_factory=list,
        metadata={
            "name": "Occurrence",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    occurrence_group: List["OccurrenceGroup"] = field(
        default_factory=list,
        metadata={
            "name": "OccurrenceGroup",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
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
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Point3Dlist(Point3DlistT):
    """
    A list of positions in 3D space.
    """
    class Meta:
        name = "Point3DList"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Positions(Point3DlistT):
    """
    3 3D-Points defining the circum circle.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class RefPlanesT(ReferencePlaneT):
    """
    Frame table position definition.

    Attributes
        ref_plane:
        origin: The origin of a local or global coordinate system. If
            not given, it is assumed thet the origin of the reference
            system at the global origin (0,0,0).
        is_main_system: True if this is the main reference system
            definition.
    """
    class Meta:
        name = "RefPlanes_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_plane: List[RefPlane] = field(
        default_factory=list,
        metadata={
            "name": "RefPlane",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    is_main_system: bool = field(
        default=True,
        metadata={
            "name": "isMainSystem",
            "type": "Attribute",
        }
    )


@dataclass
class SingleBracket(SingleBracketT):
    """
    Double bracket connection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SlotParameters(SlotParametersT):
    """
    Parameters of a slot (cut-out) typically used in shipbuilding.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Transformation(TransformationT):
    """A concept specifying a local (orthogonal) axis system.

    The Origin and two of the local X,Y,Z axis have to be specified.
    When used to specify a Plane the XY (UV) plane is considered. The
    third axis is found by the cross product of the primary and
    secondary axis.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Xgrid(XgridT):
    """
    The Vessel X coordinate system organised as a frame table or X-grid.
    """
    class Meta:
        name = "XGrid"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Ygrid(YgridT):
    """
    The definition of the vessel Y grid system.
    """
    class Meta:
        name = "YGrid"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Zgrid(ZgridT):
    """
    The definition of the vessel Z grid system.
    """
    class Meta:
        name = "ZGrid"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DimensionSet(DimensionSetType):
    """
    Container for dimensions.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class UnitType:
    """
    Type for the unit.

    Attributes
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
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    unit_name: List[UnitName] = field(
        default_factory=list,
        metadata={
            "name": "UnitName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "min_occurs": 1,
        }
    )
    unit_symbol: List[UnitSymbol] = field(
        default_factory=list,
        metadata={
            "name": "UnitSymbol",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )
    root_units: Optional[RootUnits] = field(
        default=None,
        metadata={
            "name": "RootUnits",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )
    dimension_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "dimensionURL",
            "type": "Attribute",
        }
    )


@dataclass
class BoundedRefT(EntityRefBaseT):
    """
    A bounded object reference type.
    """
    class Meta:
        name = "BoundedRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    bounding_box: Optional[BoundingBox] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class CircumCircle3DT(Curve3DT):
    """
    Type definition of a circle in 3D space defined by by a circumscribe of 3
    points.
    """
    class Meta:
        name = "CircumCircle3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    positions: Optional[Positions] = field(
        default=None,
        metadata={
            "name": "Positions",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class ControlPtListT:
    """
    Type definition of  the array of NURBS control points.

    Attributes
        control_point: The number of control points mist be minimum 2.
            The control point is composed of point in 3D space and an
            optional weight.
    """
    class Meta:
        name = "ControlPtList_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    control_point: List[ControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "ControlPoint",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 2,
        }
    )


@dataclass
class CylindricalAxes(CylindricalAxesT):
    """
    Cylindrical reference system.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Hole2DcontourT(GeometryRepresentationT):
    """
    Type definition of Parametric or curve based 2D contours.
    """
    class Meta:
        name = "Hole2DContour_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    hole_ref: Optional[HoleRef] = field(
        default=None,
        metadata={
            "name": "HoleRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class OccurrenceGroup(OccurrenceGroupT):
    """A grouping of occurrences.

    Can also contain other OccurrenceGroup to form a nested level of
    groups.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PolyLine3DT(Curve3DT):
    """
    Type definition of a 3D curve defined by a list of 3D points composing a list
    of linear segments.

    Attributes
        point3_dlist:
        is_closed: If set to true, the PolyLine3D forms a closed
            contour. The default is false.
    """
    class Meta:
        name = "PolyLine3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    point3_dlist: Optional[Point3Dlist] = field(
        default=None,
        metadata={
            "name": "Point3DList",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    is_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isClosed",
            "type": "Attribute",
        }
    )


@dataclass
class RadialPlanes(RefPlanesT):
    """
    Cylindrical reference system.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StructurePartT(EntityBaseT):
    """
    Type definition of  the abstract base class for structure objects representing
    structure concepts.
    """
    class Meta:
        name = "StructurePart_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    physical_properties: Optional[PhysicalProperties] = field(
        default=None,
        metadata={
            "name": "PhysicalProperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class VesselGridT:
    """
    The type definition of the VesselGrid.
    """
    class Meta:
        name = "VesselGrid_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    xgrid: List[Xgrid] = field(
        default_factory=list,
        metadata={
            "name": "XGrid",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ygrid: List[Ygrid] = field(
        default_factory=list,
        metadata={
            "name": "YGrid",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    zgrid: List[Zgrid] = field(
        default_factory=list,
        metadata={
            "name": "ZGrid",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class XrefPlanes(RefPlanesT):
    """The definition of the frame table positions in the Vessel X-direction.

    The authoring application must export ALL the RefPlane positions.
    If more than one XRefPlanes definition is exported, the authoring
    application shall identify the main reference system by setting the
    isMainSytem=true. It is also possible to give a reversed frame
    system (positions are given Fore to Aft). This is specified by
    setting isReversed=true.

    Attributes
        distance_to_ap:
        is_reveresed: For most vessels the X reference prositions are
            given aft to forward which is the default. Set
            isReversed=true if  the frame positions are given from fore
            to aft  (noramally this is the case for naval vessels).
    """
    class Meta:
        name = "XRefPlanes"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    distance_to_ap: Optional[DistanceToAp] = field(
        default=None,
        metadata={
            "name": "DistanceToAP",
            "type": "Element",
        }
    )
    is_reveresed: bool = field(
        default=False,
        metadata={
            "name": "isReveresed",
            "type": "Attribute",
        }
    )


@dataclass
class YrefPlanes(RefPlanesT):
    """The definition of a reference grid in the Vessel Y-direction.

    The authoring application must export ALL the RefPlane positions.
    If more than one YRefPlanes definition is exported, the authoring
    application shall identify the main reference system by setting the
    isMainSytem=true.
    """
    class Meta:
        name = "YRefPlanes"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ZrefPlanes(RefPlanesT):
    """The definition of a reference grid in the Vessel Z-direction.

    The authoring application must export ALL the RefPlane positions.
    If more than one ZRefPlanes definition is exported, the authoring
    application shall identify the main reference system by setting the
    sMainSytem=true.
    """
    class Meta:
        name = "ZRefPlanes"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Unit(UnitType):
    """Element for describing units.

    Use in containers UnitSet or directly incorporate into a host
    schema.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class CellBoundaryT(BoundedRefT):
    """
    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "CellBoundary_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PANEL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class CellRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a Cell instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "CellRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_CELL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class CircumCircle3D(CircumCircle3DT):
    """
    Definition of a circle in 3D space by a circumcircle of 3 points.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ControlPtList(ControlPtListT):
    """List of control points (X,Y,Z) and their optional weights.

    The array length N=degree+1. A minimum of 2 control points is
    necessary to define a curve.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FrameTablesT:
    """
    Type definition of FrameTables definition.

    Attributes
        xref_planes: Frame table positions along X axis. Used to limit
            geometry and define topology.
        yref_planes:
        zref_planes:
    """
    class Meta:
        name = "FrameTables_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    xref_planes: List[XrefPlanes] = field(
        default_factory=list,
        metadata={
            "name": "XRefPlanes",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    yref_planes: List[YrefPlanes] = field(
        default_factory=list,
        metadata={
            "name": "YRefPlanes",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    zref_planes: List[ZrefPlanes] = field(
        default_factory=list,
        metadata={
            "name": "ZRefPlanes",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class GridRefT(BoundedRefT):
    """A type that makes a reference to a grid definition.

    An offset along the grid reference normal vector can be given.

    Attributes
        offset:
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "GridRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_GRID_REF,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Hole2Dcontour(Hole2DcontourT):
    """
    An instantiated hole defined by a reference to a hole-shape and a
    transformation..
    """
    class Meta:
        name = "Hole2DContour"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OcxItemPtrT(BoundedRefT):
    """
    A generic type used to reference an instantiated OCX object by a GUID (the
    pointer type).

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "OcxItemPtr_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: Optional[RefTypeValue] = field(
        default=None,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class PanelRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a Bracket instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "PanelRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PANEL,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class PillarRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a pillar  instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "PillarRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PILLAR,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class PlateRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a Bracket instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "PlateRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_PLATE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class PolyLine3D(PolyLine3DT):
    """A list of 3D points defining a sequence of linear segments.

    Repeat the first position at the end of the last line segment to
    form a closed contour.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ProductViewT(DescriptionBaseT):
    """
    Abstract type definition for the ProductView.
    """
    class Meta:
        name = "ProductView_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    root_ref: Optional[RootRef] = field(
        default=None,
        metadata={
            "name": "RootRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    occurrence: List[Occurrence] = field(
        default_factory=list,
        metadata={
            "name": "Occurrence",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    occurrence_group: List[OccurrenceGroup] = field(
        default_factory=list,
        metadata={
            "name": "OccurrenceGroup",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ReferencePlanesT:
    """
    Type definition of the ReferencePlanes element.

    Attributes
        xref_planes: Frame table positions along X axis. Used to limit
            geometry and define topology.
        yref_planes:
        zref_planes:
    """
    class Meta:
        name = "ReferencePlanes_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    xref_planes: List[XrefPlanes] = field(
        default_factory=list,
        metadata={
            "name": "XRefPlanes",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    yref_planes: List[YrefPlanes] = field(
        default_factory=list,
        metadata={
            "name": "YRefPlanes",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    zref_planes: List[ZrefPlanes] = field(
        default_factory=list,
        metadata={
            "name": "ZRefPlanes",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class SeamRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a Bracket instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "SeamRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_SEAM,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SlotContour(Hole2DcontourT):
    """
    An optional contour for the detailed slot shape given as a reference to a
    catalogue shape with a transformation.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StiffenerRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a Bracket instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "StiffenerRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_STIFFENER,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SurfaceRefT(BoundedRefT):
    """
    Type definition of A OcxItemPtr reference to a Surface instance.

    Attributes
        ref_type: Allowable OCX types which can be referenced using the
            ocxItemPtr.
    """
    class Meta:
        name = "SurfaceRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ref_type: RefTypeValue = field(
        init=False,
        default=RefTypeValue.OCX_SURFACE,
        metadata={
            "name": "refType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class VesselGrid(VesselGridT):
    """
    The defintion of the vessel grid system including the vessel frame table.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UnitSetType:
    """
    Type for the unit container.

    Attributes
        unit: Element for describing units. Use in containers UnitSet or
            directly incorporate into a host schema.
    """
    class Meta:
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    unit: List[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
            "min_occurs": 1,
        }
    )


@dataclass
class CellBoundary(CellBoundaryT):
    """
    The reference to a Panel surface making up one Cell boundary.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CellRef(CellRefT):
    """
    A reference to a Compartment cell.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class DesignViewT(ProductViewT):
    """
    The type definition of the DesignView.
    """
    class Meta:
        name = "DesignView_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FrameTables(FrameTablesT):
    """The Vessel reference coordinate system organised as a frame table system.

    The authoring system must export the complete frame table definition
    for ALL X, Y and Z positions. The FrameTables may define several X,
    Y, or Z systems. As a minimum, each main system must be exported. If
    more than one system is exported, the authoring system must set the
    isMainSystem=true for the main reference system in each direction.
    This definition is kept for backward compatibility from schema
    version 2.8.6. It might change in a future schema version.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class GridRef(GridRefT):
    """An element that makes a reference to a grid definition.

    An offset along the grid reference normal vector can be given.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Nurbs3DT(Curve3DT):
    """
    Type definition of a Non-uniform rational basis spline (NURBS) curve defined by
    a set of 3D control points.
    """
    class Meta:
        name = "NURBS3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    nurbsproperties: Optional[Nurbsproperties] = field(
        default=None,
        metadata={
            "name": "NURBSproperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    knot_vector: Optional[KnotVector] = field(
        default=None,
        metadata={
            "name": "KnotVector",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    control_pt_list: Optional[ControlPtList] = field(
        default=None,
        metadata={
            "name": "ControlPtList",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class OcxItemPtr(OcxItemPtrT):
    """
    A generic element used to reference an instantiated OCX object by a GUID (the
    pointer).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PanelRef(PanelRefT):
    """
    The reference to a connected Plate.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PillarRef(PillarRefT):
    """
    The reference to a connected Member (Pillar).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PlateRef(PlateRefT):
    """
    The reference to a connected Plate.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ReferencePlanes(ReferencePlanesT):
    """
    The collection of refrence planes used to limit geometries.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SeamRef(SeamRefT):
    """
    The reference to a connected Plate.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StiffenerRef(StiffenerRefT):
    """
    A OcxItemPtr reference to a Stiffener.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SurfaceRef(SurfaceRefT):
    """
    The reference to a Surface geometry which is shared between more than one part.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebStiffenerRefT(StiffenerRefT):
    """
    Type definition of WebStiffener connection.

    Attributes
        position: The position of the web stiffener relative to the
            penetrating stiffener end.
    """
    class Meta:
        name = "WebStiffenerRef_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    position: Optional[PositionValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class UnitSet(UnitSetType):
    """Container for units.

    Use in UnitsML container or directly incorporate into a host schema.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class CellConnectionT:
    """
    Type definition for connecting cells to a compartment.

    Attributes
        cell_ref: A reference to the two connected compartment cells.
    """
    class Meta:
        name = "CellConnection_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    cell_ref: List[CellRef] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )


@dataclass
class CellT(GeometryRepresentationT):
    """
    Type definition of the structural concept of a cell defining a part of a
    compartment (physical space).
    """
    class Meta:
        name = "Cell_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    cell_boundary: List[CellBoundary] = field(
        default_factory=list,
        metadata={
            "name": "CellBoundary",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class CoordinateSystemT(EntityBaseT):
    """
    Type definition of the vessel coordinate system A right-handed orthogonal
    Cartesian co-ordinate system.

    Attributes
        local_cartesian:
        frame_tables: The Vessel reference coordinate system organised
            as a frame table system. The authoring system must export
            the complete frame table definition for ALL X, Y and Z
            positions. The FrameTables may define several X, Y, or Z
            systems. As a minimum, each main system must be exported. If
            more than one system is exported, the authoring system must
            set the isMainSystem=true for the main reference system in
            each direction.
        vessel_grid:
        is_global: If set to true, the coordinate system is the global
            world coordinate frame with right handed convention. This is
            the default.
    """
    class Meta:
        name = "CoordinateSystem_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    local_cartesian: List[LocalCartesian] = field(
        default_factory=list,
        metadata={
            "name": "LocalCartesian",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    frame_tables: List[FrameTables] = field(
        default_factory=list,
        metadata={
            "name": "FrameTables",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    vessel_grid: List[VesselGrid] = field(
        default_factory=list,
        metadata={
            "name": "VesselGrid",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    is_global: bool = field(
        default=True,
        metadata={
            "name": "isGlobal",
            "type": "Attribute",
        }
    )


@dataclass
class DesignView(DesignViewT):
    """
    A manifestation of some or all the components in the exporting application that
    contains configuration information for the parts it includes.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Nurbs3D(Nurbs3DT):
    """
    Non-Uniform Rational Spline Base curve definition.
    """
    class Meta:
        name = "NURBS3D"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PentetratingObjectT:
    """
    Type definition of a penetrated structural object.

    Attributes
        plate_ref: Reference to a a penetrated Plate.
        slot_parameters:
    """
    class Meta:
        name = "PentetratingObject_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    plate_ref: Optional[PlateRef] = field(
        default=None,
        metadata={
            "name": "PlateRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    slot_parameters: Optional[SlotParameters] = field(
        default=None,
        metadata={
            "name": "SlotParameters",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class WebStiffenerRef(WebStiffenerRefT):
    """
    Web stiffener connection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UnitsMltype:
    """
    ComplexType for the root element of an UnitsML document.
    """
    class Meta:
        name = "UnitsMLType"
        target_namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"

    unit_set: Optional[UnitSet] = field(
        default=None,
        metadata={
            "name": "UnitSet",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )
    dimension_set: Optional[DimensionSet] = field(
        default=None,
        metadata={
            "name": "DimensionSet",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )


@dataclass
class Cell(CellT):
    """
    Structural concept of a cell defining a closed volume which is part of a
    compartment (physical space).
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CellConnection(CellConnectionT):
    """
    Cross flow connection between two cells.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CompositeCurve3DT(Curve3DT):
    """
    Type definition of a composite curve composed of a collection of Line3D,
    CircumArc3D and/or NURBS segments..

    Attributes
        line3_d:
        circum_arc3_d:
        nurbs3_d:
        poly_line3_d: A list of 3D points defining a list of linear
            segments. Repeat the first position at the end to form a
            closed contour.
    """
    class Meta:
        name = "CompositeCurve3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    line3_d: List[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_arc3_d: List[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbs3_d: List[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poly_line3_d: List[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class CoordinateSystem(CoordinateSystemT):
    """A right-handed orthogonal Cartesian co-ordinate system.

    Used to define the vessel coordinate system definition..
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebStiffenerWithDoubleBracketT:
    """
    Type definition of Web stiffener with double bracket connection.

    Attributes
        connected_bracket_ref: Reference to the two connected brackets
            which are part of a ConnectionConfiguration.
        web_stiffener_ref:
    """
    class Meta:
        name = "WebStiffenerWithDoubleBracket_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    connected_bracket_ref: List[ConnectedBracketRef] = field(
        default_factory=list,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    web_stiffener_ref: Optional[WebStiffenerRef] = field(
        default=None,
        metadata={
            "name": "WebStiffenerRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class WebStiffenerWithSingleBracketT:
    """
    Type definition of Web stiffener with single bracket connection.
    """
    class Meta:
        name = "WebStiffenerWithSingleBracket_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    connected_bracket_ref: Optional[ConnectedBracketRef] = field(
        default=None,
        metadata={
            "name": "ConnectedBracketRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    web_stiffener_ref: Optional[WebStiffenerRef] = field(
        default=None,
        metadata={
            "name": "WebStiffenerRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class WebStiffenerT:
    """
    Type definition of Web stiffener with single bracket connection.
    """
    class Meta:
        name = "WebStiffener_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    web_stiffener_ref: Optional[WebStiffenerRef] = field(
        default=None,
        metadata={
            "name": "WebStiffenerRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class UnitsMl(UnitsMltype):
    """
    Container for UnitsML units, quantities, and prefixes.
    """
    class Meta:
        name = "UnitsML"
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class BaseCurve(CompositeCurve3DT):
    """
    The base curve defining an extruded surface when it is swept.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CompositeCurve3D(CompositeCurve3DT):
    """The concept of a composite curve composed of a collection of Line3D,
    CircumArc3D and/or NURBS segments.

    Curves are sorted end to end and have C1 continuity across each
    segment in the CompositeCurve3D definition.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CrossFlowT(IdBaseT):
    """
    Type definition of the concept specifying cross flow between Cells making up an
    Compartment.
    """
    class Meta:
        name = "CrossFlow_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    cell_connection: Optional[CellConnection] = field(
        default=None,
        metadata={
            "name": "CellConnection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SweepCurve(CompositeCurve3DT):
    """
    The sweep direction and extent is defined by a general 3D sweep curve.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebStiffener(WebStiffenerT):
    """
    Connsction configuration with one web stiffener with a single bracket
    connection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebStiffenerWithDoubleBracket(WebStiffenerWithDoubleBracketT):
    """
    Web stiffener with double bracket connection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebStiffenerWithSingleBracket(WebStiffenerWithSingleBracketT):
    """
    Connsction configuration with one web stiffener with a single bracket
    connection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ConnectionConfigurationT(DescriptionBaseT):
    """
    Type definition of the structural concept defining  end configurations for
    stiffeners used in shipbuilding.

    Attributes
        point3_d: The logical geometric position of the end
            configuration at the stiffener's end.
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
        stiffener_ref: The rference to the connected Stiffener at this
            end configuration.
    """
    class Meta:
        name = "ConnectionConfiguration_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    point3_d: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Point3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    single_bracket: Optional[SingleBracket] = field(
        default=None,
        metadata={
            "name": "SingleBracket",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    double_bracket: Optional[DoubleBracket] = field(
        default=None,
        metadata={
            "name": "DoubleBracket",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    web_stiffener: Optional[WebStiffener] = field(
        default=None,
        metadata={
            "name": "WebStiffener",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    web_stiffener_with_single_bracket: Optional[WebStiffenerWithSingleBracket] = field(
        default=None,
        metadata={
            "name": "WebStiffenerWithSingleBracket",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    web_stiffener_with_double_bracket: Optional[WebStiffenerWithDoubleBracket] = field(
        default=None,
        metadata={
            "name": "WebStiffenerWithDoubleBracket",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    plate_ref: Optional[PlateRef] = field(
        default=None,
        metadata={
            "name": "PlateRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    pillar_ref: Optional[PillarRef] = field(
        default=None,
        metadata={
            "name": "PillarRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    stiffener_ref: Optional[StiffenerRef] = field(
        default=None,
        metadata={
            "name": "StiffenerRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Contour3DT:
    """
    The geometry of a closed contour limiting a surface, represented by a set of
    trim curves or a closed curve primitive.
    """
    class Meta:
        name = "Contour3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    ellipse3_d: Optional[Ellipse3D] = field(
        default=None,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_circle3_d: Optional[CircumCircle3D] = field(
        default=None,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circle3_d: Optional[Circle3D] = field(
        default=None,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_arc3_d: List[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    line3_d: List[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    composite_curve3_d: List[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poly_line3_d: List[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbs3_d: List[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class CrossFlow(CrossFlowT):
    """Concept to specify cross flow between Cells making up a Compartment.

    This enables the modelling of cells that are not adjacent but are
    connected by a piping system and part of the same Compartment.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FreeEdgeCurve3DT(EntityBaseT):
    """
    The type definition of a free edge defined by a collection of non-closed
    Curve3D types.

    Attributes
        circum_arc3_d:
        line3_d:
        composite_curve3_d:
        poly_line3_d:
        nurbs3_d:
        is_uvspace: Default is flase. Set this attribute to to true if
            the FreeEdgeCurve is represnted by coordinates in the UV
            space. This should only be used when a FreeEdgeCurve is used
            to trim NURBS surface patches where the trim curve is only
            used to trim the underlying surface. When the curve is given
            in UV space, the X,Y point coordinates are replazed with the
            U,V coordinates. In this case the Z coordinate should be set
            to zero. The Z coordinate will not be used by the importing
            application.
    """
    class Meta:
        name = "FreeEdgeCurve3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    circum_arc3_d: List[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    line3_d: List[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    composite_curve3_d: List[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poly_line3_d: List[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbs3_d: List[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    is_uvspace: bool = field(
        default=False,
        metadata={
            "name": "isUVSpace",
            "type": "Attribute",
        }
    )


@dataclass
class TraceLineT:
    """
    The type definition of the stiffener TraceLine.
    """
    class Meta:
        name = "TraceLine_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    circum_arc3_d: List[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbs3_d: List[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ellipse3_d: List[Ellipse3D] = field(
        default_factory=list,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_circle3_d: List[CircumCircle3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circle3_d: List[Circle3D] = field(
        default_factory=list,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    composite_curve3_d: List[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    line3_d: List[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poly_line3_d: List[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class BarSectionContour(Contour3DT):
    """
    A closed contour of the stiffener end cut representing the tre stiffener
    geometry.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ConnectionConfiguration(ConnectionConfigurationT):
    """
    The structural concept defining the end configurations for stiffeners used in
    shipbuilding.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Contour(Contour3DT):
    """
    The contour of a surface or structure part.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class EndCutContour(Contour3DT):
    """
    A closed contour of the stiffener end cut representing the negative stiffener
    end cut geometry.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FaceBoundaryCurve(Contour3DT):
    """
    A collection of 3D curves making up a closed boundary.

    Attributes
        is_uvspace: If set to True, the FacBoundaryCurve is defined in
            the parametric UV space. The Pont3D X and Y correspnds to U
            and V while the Z coordinate is disregarded. The default is
            False, i.e. the FaceBoundaryCurve is defined in the 3D
            space.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    is_uvspace: object = field(
        default="False",
        metadata={
            "name": "isUVspace",
            "type": "Attribute",
        }
    )


@dataclass
class FlangeContour(Contour3DT):
    """The outer contour of a stiffener flange.

    The FlangeContour can be used to render the shape of a BarSection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class FreeEdgeCurve3D(FreeEdgeCurve3DT):
    """
    A single Curve3D or a collection of continuous non-closed Curve3D types which
    are used to represent a free edge of a panel or plate in shipbuilding.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class InnerContour(Contour3DT):
    """
    Any closed contour of an inner opening in a plate.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OuterContour(Contour3DT):
    """
    The geometry of the outer closed contour limiting a surface, represented by a
    set of trim curves or a closed curve primitive.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PenetrationT(ConnectionConfigurationT):
    """
    Type definition of Structural concept of stiffener penetration configurations
    typically used in shipbuilding.

    Attributes
        slot_parameters:
        tightness: The tightness type of the penetration.
    """
    class Meta:
        name = "Penetration_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    slot_parameters: Optional[SlotParameters] = field(
        default=None,
        metadata={
            "name": "SlotParameters",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    tightness: Optional[TightnessValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class PhysicalSpaceT(EntityBaseT):
    """
    Type definition of the  concept of a physical compartment representing a closed
    volume (space) defined by  enclosing  structure panels.

    Attributes
        compartment_properties:
        cell:
        cross_flow: Specify cross flow between Cells making up an
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    compartment_properties: Optional[CompartmentProperties] = field(
        default=None,
        metadata={
            "name": "CompartmentProperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    cell: List[Cell] = field(
        default_factory=list,
        metadata={
            "name": "Cell",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    cross_flow: List[CrossFlow] = field(
        default_factory=list,
        metadata={
            "name": "CrossFlow",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulk_cargo: List[BulkCargo] = field(
        default_factory=list,
        metadata={
            "name": "BulkCargo",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    liquid_cargo: List[LiquidCargo] = field(
        default_factory=list,
        metadata={
            "name": "LiquidCargo",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    unit_cargo: List[UnitCargo] = field(
        default_factory=list,
        metadata={
            "name": "UnitCargo",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    compartment_purpose: Optional[CompartmentPurposeValue] = field(
        default=None,
        metadata={
            "name": "compartmentPurpose",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class SectionInnerShape(Contour3DT):
    """
    Optional arbitrary inner section shape for hollow sections.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SectionOuterShape(Contour3DT):
    """An optional arbitrary contour  representing the outer section shape.

    Used to display the section by extrusion of the section shape along
    the trace line.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class TraceLine(TraceLineT):
    """
    The landing curve on the moulded panel surface represented by any Curve3D type.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class WebContour(Contour3DT):
    """The outer contour of a stiffener web.

    The WebContour can be used to render the shape of a BarSection.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CutByT:
    """
    Type definition of  a structural concept defining a cut-out in a surface
    defined by a parametric hole or a set of generic trim curves.
    """
    class Meta:
        name = "CutBy_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    inner_contour: List[InnerContour] = field(
        default_factory=list,
        metadata={
            "name": "InnerContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    hole2_dcontour: List[Hole2Dcontour] = field(
        default_factory=list,
        metadata={
            "name": "Hole2DContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    slot_contour: Optional[SlotContour] = field(
        default=None,
        metadata={
            "name": "SlotContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class EdgeReinforcementT(StructurePartT):
    class Meta:
        name = "EdgeReinforcement_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    material_ref: Optional[MaterialRef] = field(
        default=None,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    inclination: Optional[Inclination] = field(
        default=None,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    edge_curve_ref: List[EdgeCurveRef] = field(
        default_factory=list,
        metadata={
            "name": "EdgeCurveRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Hole2D(Hole2DT):
    """
    A 2D hole shape defined either by a parametric hole or a curve contour.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    rectangular_hole: Optional[RectangularHole] = field(
        default=None,
        metadata={
            "name": "RectangularHole",
            "type": "Element",
        }
    )
    super_elliptical: Optional[SuperElliptical] = field(
        default=None,
        metadata={
            "name": "SuperElliptical",
            "type": "Element",
        }
    )
    symmetrical_hole: Optional[SymmetricalHole] = field(
        default=None,
        metadata={
            "name": "SymmetricalHole",
            "type": "Element",
        }
    )
    parametric_circle: Optional[ParametricCircle] = field(
        default=None,
        metadata={
            "name": "ParametricCircle",
            "type": "Element",
        }
    )
    contour: Optional[Contour] = field(
        default=None,
        metadata={
            "name": "Contour",
            "type": "Element",
        }
    )


@dataclass
class LimitedByT:
    """
    Type definition of the LimitedBy (reference to limiting objects forming a
    closed contour of the parent element).

    Attributes
        free_edge_curve3_d: Collection of non-closed Curve3D types. Used
            to represent a free edge to form a closed contour together
            with the limiting objects.
        ocx_item_ptr: A generic element used to reference an
            instantiated OCX object by a GUID (the pointer).
        grid_ref:
    """
    class Meta:
        name = "LimitedBy_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    free_edge_curve3_d: List[FreeEdgeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "FreeEdgeCurve3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ocx_item_ptr: List[OcxItemPtr] = field(
        default_factory=list,
        metadata={
            "name": "OcxItemPtr",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    grid_ref: List[GridRef] = field(
        default_factory=list,
        metadata={
            "name": "GridRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Penetration(PenetrationT):
    """
    Structural concept of stiffener penetration configurations typically used in
    shipbuilding.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PhysicalSpace(PhysicalSpaceT):
    """
    The concept of a physical compartment representing a closed volume (space)
    defined by  enclosing  structure panels.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SeamT(EntityBaseT):
    """
    Type definition of the Seam element describing plate seams.
    """
    class Meta:
        name = "Seam_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_arc3_d: List[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbs3_d: List[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ellipse3_d: List[Ellipse3D] = field(
        default_factory=list,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_circle3_d: List[CircumCircle3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circle3_d: List[Circle3D] = field(
        default_factory=list,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    composite_curve3_d: List[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    line3_d: List[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poly_line3_d: List[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class SurfaceT(GeometryRepresentationT):
    """
    Type definition of the  Abstract base class for surface definitions.

    Attributes
        area:
        face_boundary_curve: A collection of 3D curves making up a
            closed boundary. To be used whenever the surface need to be
            bounded.
    """
    class Meta:
        name = "Surface_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    area: Optional[Area] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    face_boundary_curve: Optional[FaceBoundaryCurve] = field(
        default=None,
        metadata={
            "name": "FaceBoundaryCurve",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class UserDefinedBarSectionT:
    """
    Attributes
        section_properties:
        user_defined_parameter: Any number of additional user-defined
            parameters. The intended use and how the parameter shall be
            interpreted shall be included in the description.
        section_outer_shape:
        section_inner_shape:
        number_of_parameters: Number of additional user-defined
            parameters included in the definition.
    """
    class Meta:
        name = "UserDefinedBarSection_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    section_properties: Optional[SectionProperties] = field(
        default=None,
        metadata={
            "name": "SectionProperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    user_defined_parameter: List[UserDefinedParameter] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedParameter",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    section_outer_shape: Optional[SectionOuterShape] = field(
        default=None,
        metadata={
            "name": "SectionOuterShape",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    section_inner_shape: Optional[SectionInnerShape] = field(
        default=None,
        metadata={
            "name": "SectionInnerShape",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    number_of_parameters: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfParameters",
            "type": "Attribute",
        }
    )


@dataclass
class Cone3DT(SurfaceT):
    """
    Type definition of the a Cone surface defined by origin,  radius and position
    of cone tip.

    Attributes
        origin: The origin or centre of the cone at the base.
        tip:
        base_radius:
        tip_radius: Cone tip radius (default = 0).
    """
    class Meta:
        name = "Cone3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    tip: Optional[Tip] = field(
        default=None,
        metadata={
            "name": "Tip",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    base_radius: Optional[BaseRadius] = field(
        default=None,
        metadata={
            "name": "BaseRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    tip_radius: Optional[TipRadius] = field(
        default=None,
        metadata={
            "name": "TipRadius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class CutBy(CutByT):
    """
    A structural concept defining a cut-out in a surface defined by a parametric
    hole or a set of generic trim curves.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Cylinder3DT(SurfaceT):
    """
    Type definition of the cylindrical surface defined by root point, axis
    direction, radius and height.

    Attributes
        origin: Cylinder anchor position.
        axis:
        radius: Cylinder radius.
        height: Cylinder height relative to origin.
    """
    class Meta:
        name = "Cylinder3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    axis: Optional[Axis] = field(
        default=None,
        metadata={
            "name": "Axis",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    height: Optional[Height] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class EdgeReinforcement(EdgeReinforcementT):
    """An EdgeReinforement is used as a face-plate or edge reinforcement for a
    Panel, Plate or Bracket.

    The EfgeReinforcement is composed of a BarSection (usually a flat
    bar profile) and is attached to a FreeEdgeCurve which is part of the
    Panel or Plate LimitedBy. The EdgeReinforcement can reference one or
    more limits for the Panel/Plate/Bracket. At the same time the
    EdgeReinforcement provides it's own TraceLine to determine the
    actual exctent of the reinforcement.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ExtrudedSurfaceT(SurfaceT):
    """
    Type definition of an extruded surface defined by a base curve and a sweep path
    with extent.
    """
    class Meta:
        name = "ExtrudedSurface_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    base_curve: Optional[BaseCurve] = field(
        default=None,
        metadata={
            "name": "BaseCurve",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    sweep: Optional[Sweep] = field(
        default=None,
        metadata={
            "name": "Sweep",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    sweep_curve: Optional[SweepCurve] = field(
        default=None,
        metadata={
            "name": "SweepCurve",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class HoleShapeCatalogueT(DescriptionBaseT):
    """
    Type definition of the geometry used to describe the shape of a hole.

    Attributes
        hole2_d: 2D hole definition based on either a geometric or
            parametric definition.
    """
    class Meta:
        name = "HoleShapeCatalogue_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    hole2_d: List[Hole2D] = field(
        default_factory=list,
        metadata={
            "name": "Hole2D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class LimitedBy(LimitedByT):
    """The references to limiting objects forming a closed contour of the parent
    element.

    It is not requiredthat the set of objects is ordered in the correct
    sequence.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class NurbssurfaceT(SurfaceT):
    """
    Type definition of a Non-uniform rational basis surface definition defined by a
    grid of 3D control points.

    Attributes
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    u_nurbsproperties: Optional[UNurbsproperties] = field(
        default=None,
        metadata={
            "name": "U_NURBSproperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    uknot_vector: Optional[UknotVector] = field(
        default=None,
        metadata={
            "name": "UknotVector",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    v_nurbsproperties: Optional[VNurbsproperties] = field(
        default=None,
        metadata={
            "name": "V_NURBSproperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    vknot_vector: Optional[VknotVector] = field(
        default=None,
        metadata={
            "name": "VknotVector",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    control_pt_list: List[ControlPtList] = field(
        default_factory=list,
        metadata={
            "name": "ControlPtList",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class Seam(SeamT):
    """
    Element describing the structure concept of a plate seam.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Sphere3DT(SurfaceT):
    """
    Type definition of a Spherical surface defined by origin and radius.
    """
    class Meta:
        name = "Sphere3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    radius: Optional[Radius] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class UserDefinedBarSection(UserDefinedBarSectionT):
    """
    User defined or unknown bar type.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BarSectionT(DescriptionBaseT):
    """
    Type definition of the  catalogue of rolled and welded cross sections
    recognised by the Society.

    Attributes
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
        manufacture: Manufacturing method.
        guidref:
    """
    class Meta:
        name = "BarSection_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    rectangular_tube: Optional[RectangularTube] = field(
        default=None,
        metadata={
            "name": "RectangularTube",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    octagon_bar: Optional[OctagonBar] = field(
        default=None,
        metadata={
            "name": "OctagonBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    square_bar: Optional[SquareBar] = field(
        default=None,
        metadata={
            "name": "SquareBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulb_flat: Optional[BulbFlat] = field(
        default=None,
        metadata={
            "name": "BulbFlat",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    flat_bar: Optional[FlatBar] = field(
        default=None,
        metadata={
            "name": "FlatBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ubar: Optional[Ubar] = field(
        default=None,
        metadata={
            "name": "UBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ibar: Optional[Ibar] = field(
        default=None,
        metadata={
            "name": "IBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    lbar_of: Optional[LbarOf] = field(
        default=None,
        metadata={
            "name": "LBarOF",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    zbar: Optional[Zbar] = field(
        default=None,
        metadata={
            "name": "ZBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    round_bar: Optional[RoundBar] = field(
        default=None,
        metadata={
            "name": "RoundBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    lbar: Optional[Lbar] = field(
        default=None,
        metadata={
            "name": "LBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    tbar: Optional[Tbar] = field(
        default=None,
        metadata={
            "name": "TBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    lbar_ow: Optional[LbarOw] = field(
        default=None,
        metadata={
            "name": "LBarOW",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    half_round_bar: Optional[HalfRoundBar] = field(
        default=None,
        metadata={
            "name": "HalfRoundBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    hexagon_bar: Optional[HexagonBar] = field(
        default=None,
        metadata={
            "name": "HexagonBar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    tube: Optional[Tube] = field(
        default=None,
        metadata={
            "name": "Tube",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    user_defined_bar_section: Optional[UserDefinedBarSection] = field(
        default=None,
        metadata={
            "name": "UserDefinedBarSection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortID",
            "type": "Attribute",
        }
    )
    manufacture: Optional[BarSectionTManufacture] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class Cone3D(Cone3DT):
    """
    Cone surface defined by origin, radius and position of cone tip.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Cylinder3D(Cylinder3DT):
    """
    Cylindrical surface defined by origin, axis direction, radius and height.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ExtrudedSurface(ExtrudedSurfaceT):
    """
    An extruded surface defined by a base curve and a sweep path with extent.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class HoleShapeCatalogue(HoleShapeCatalogueT):
    """
    Catalogue of 2D hole shapes.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class MemberT(StructurePartT):
    """
    Abstract type definition for the Member element.
    """
    class Meta:
        name = "Member_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Nurbssurface(NurbssurfaceT):
    """
    Non-uniform rational basis surface definition defined by a net (grid) of
    polynomial basis functions  in U and V direction.
    """
    class Meta:
        name = "NURBSSurface"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Plane3DT(SurfaceT):
    """
    Type definition of a  Planar surface defined by Root Point and Normal.

    Attributes
        origin:
        normal:
        udirection: Optional local U direction of the plane.
        limited_by:
    """
    class Meta:
        name = "Plane3D_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    normal: Optional[Normal] = field(
        default=None,
        metadata={
            "name": "Normal",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    udirection: Optional[Udirection] = field(
        default=None,
        metadata={
            "name": "UDirection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Sphere3D(Sphere3DT):
    """
    Spherical surface defined by origin and radius.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SplitByT:
    """
    Type definition of Structural concepts defining the subdivision of a panel into
    plates split by one or more seams.
    """
    class Meta:
        name = "SplitBy_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    seam: List[Seam] = field(
        default_factory=list,
        metadata={
            "name": "Seam",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class StiffenerT(StructurePartT):
    """
    Type definition of the Stiffener structure concept.

    Attributes
        material_ref:
        section_ref:
        trace_line:
        circum_arc3_d:
        nurbs3_d:
        ellipse3_d:
        circum_circle3_d:
        circle3_d:
        composite_curve3_d:
        line3_d:
        poly_line3_d:
        inclination:
        end_cut_end1: The stiffener end cut detailing at end 1.
        end_cut_end2: The stiffener end cut detailing at end 2.
        web_contour:
        flange_contour:
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
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    material_ref: Optional[MaterialRef] = field(
        default=None,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_arc3_d: List[CircumArc3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumArc3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbs3_d: List[Nurbs3D] = field(
        default_factory=list,
        metadata={
            "name": "NURBS3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ellipse3_d: List[Ellipse3D] = field(
        default_factory=list,
        metadata={
            "name": "Ellipse3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circum_circle3_d: List[CircumCircle3D] = field(
        default_factory=list,
        metadata={
            "name": "CircumCircle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    circle3_d: List[Circle3D] = field(
        default_factory=list,
        metadata={
            "name": "Circle3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    composite_curve3_d: List[CompositeCurve3D] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    line3_d: List[Line3D] = field(
        default_factory=list,
        metadata={
            "name": "Line3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    poly_line3_d: List[PolyLine3D] = field(
        default_factory=list,
        metadata={
            "name": "PolyLine3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    inclination: List[Inclination] = field(
        default_factory=list,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    end_cut_end1: Optional[EndCutEnd1] = field(
        default=None,
        metadata={
            "name": "EndCutEnd1",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    end_cut_end2: Optional[EndCutEnd2] = field(
        default=None,
        metadata={
            "name": "EndCutEnd2",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    web_contour: Optional[WebContour] = field(
        default=None,
        metadata={
            "name": "WebContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    flange_contour: List[FlangeContour] = field(
        default_factory=list,
        metadata={
            "name": "FlangeContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 2,
        }
    )
    offset: Optional[Offset] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    connection_configuration: List[ConnectionConfiguration] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionConfiguration",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 2,
        }
    )
    penetration: List[Penetration] = field(
        default_factory=list,
        metadata={
            "name": "Penetration",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class BarSection(BarSectionT):
    """
    A catalogue of rolled and welded cross sections recognised by the Society.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PillarT(MemberT):
    """
    Type definition of the structural concept for pillars used as vertical support
    in ship building.

    Attributes
        material_ref:
        section_ref:
        trace_line: The pillar traceline represented by a Curve3D type.
        inclination:
        cut_by:
        penetration:
        connection_configuration: The connection configuration at end 1
            and/or end 2 of the pillar.
        function_type:
    """
    class Meta:
        name = "Pillar_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    material_ref: Optional[MaterialRef] = field(
        default=None,
        metadata={
            "name": "MaterialRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    trace_line: Optional[TraceLine] = field(
        default=None,
        metadata={
            "name": "TraceLine",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    inclination: List[Inclination] = field(
        default_factory=list,
        metadata={
            "name": "Inclination",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    penetration: List[Penetration] = field(
        default_factory=list,
        metadata={
            "name": "Penetration",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    connection_configuration: List[ConnectionConfiguration] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionConfiguration",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "max_occurs": 2,
        }
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Plane3D(Plane3DT):
    """
    Planar surface defined by origin and Normal direction.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SplitBy(SplitByT):
    """
    Structural concepts defining the subdivision of a panel into plates split by
    one or more seams.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Stiffener(StiffenerT):
    """
    Element describing the structure concept of type stiffeners which are attached
    to plating and constitutes the scantlings.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Pillar(PillarT):
    """
    Structural concept for pillars used as vertical support in ship building.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class StiffenedByT:
    """
    Type definition of the structural concept defining the stiffeners which is
    belonging to a panel.
    """
    class Meta:
        name = "StiffenedBy_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    stiffener: List[Stiffener] = field(
        default_factory=list,
        metadata={
            "name": "Stiffener",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    edge_reinforcement: List[EdgeReinforcement] = field(
        default_factory=list,
        metadata={
            "name": "EdgeReinforcement",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class SurfaceCollectionT(DescriptionBaseT):
    class Meta:
        name = "SurfaceCollection_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    plane3_d: List[Plane3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbssurface: List[Nurbssurface] = field(
        default_factory=list,
        metadata={
            "name": "NURBSSurface",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    extruded_surface: List[ExtrudedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ExtrudedSurface",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    sphere3_d: List[Sphere3D] = field(
        default_factory=list,
        metadata={
            "name": "Sphere3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cone3_d: List[Cone3D] = field(
        default_factory=list,
        metadata={
            "name": "Cone3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cylinder3_d: List[Cylinder3D] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    guidref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUIDRef",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_length": 1,
            "max_length": 40,
        }
    )


@dataclass
class UnboundedGeometryT:
    """
    Type definition of an unbounded surface geometry of the parent element.
    """
    class Meta:
        name = "UnboundedGeometry_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    plane3_d: List[Plane3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbssurface: List[Nurbssurface] = field(
        default_factory=list,
        metadata={
            "name": "NURBSSurface",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    extruded_surface: List[ExtrudedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ExtrudedSurface",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    sphere3_d: List[Sphere3D] = field(
        default_factory=list,
        metadata={
            "name": "Sphere3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cone3_d: List[Cone3D] = field(
        default_factory=list,
        metadata={
            "name": "Cone3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cylinder3_d: List[Cylinder3D] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    surface_ref: Optional[SurfaceRef] = field(
        default=None,
        metadata={
            "name": "SurfaceRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    grid_ref: List[GridRef] = field(
        default_factory=list,
        metadata={
            "name": "GridRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class XsectionCatalogueT(DescriptionBaseT):
    """
    Type definition of the cross section types for stiffeners and their properties
    recognised by the Society.
    """
    class Meta:
        name = "XSectionCatalogue_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    bar_section: List[BarSection] = field(
        default_factory=list,
        metadata={
            "name": "BarSection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )


@dataclass
class CompartmentFaceT(UnboundedGeometryT):
    """
    Type definition of the face of a compartment defined by a surface boundary.

    Attributes
        face_boundary_curve: A collection of 3D curves making up the
            closed boundary of the compartment face.
    """
    class Meta:
        name = "CompartmentFace_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    face_boundary_curve: Optional[FaceBoundaryCurve] = field(
        default=None,
        metadata={
            "name": "FaceBoundaryCurve",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class StiffenedBy(StiffenedByT):
    """
    Structural concept defining the stiffeners which is belonging to a panel.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class SurfaceCollection(SurfaceCollectionT):
    """A collection of any number of surfces.

    The surfaces have to be connected (no dis-joint surfaces). Most
    typically the SurfaceCollection will include the outer shell
    geometry definition of the vessel.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class UnboundedGeometry(UnboundedGeometryT):
    """
    The unbounded surface geometry of the parent element.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class XsectionCatalogue(XsectionCatalogueT):
    """
    The cross section types for stiffeners and their properties recognised by the
    Society.
    """
    class Meta:
        name = "XSectionCatalogue"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class BracketT(StructurePartT):
    """
    Type definition  of Structural concept of brackets used in shipbuilding.
    """
    class Meta:
        name = "Bracket_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    bracket_parameters: List[BracketParameters] = field(
        default_factory=list,
        metadata={
            "name": "BracketParameters",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    plate_material: List[PlateMaterial] = field(
        default_factory=list,
        metadata={
            "name": "PlateMaterial",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    offset: List[Offset] = field(
        default_factory=list,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    outer_contour: List[OuterContour] = field(
        default_factory=list,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    unbounded_geometry: List[UnboundedGeometry] = field(
        default_factory=list,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    limited_by: List[LimitedBy] = field(
        default_factory=list,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cut_by: List[CutBy] = field(
        default_factory=list,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    inner_contour: List[InnerContour] = field(
        default_factory=list,
        metadata={
            "name": "InnerContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    stiffened_by: List[StiffenedBy] = field(
        default_factory=list,
        metadata={
            "name": "StiffenedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ClassCatalogueT(DescriptionBaseT):
    """
    Type definition of the Class catalogues provided as part of the OCX.

    Attributes
        material_catalogue: Catalogue of material types and their
            properties.
        xsection_catalogue: Catalogue of section types and their
            properties.
        hole_shape_catalogue: Catalogue of 2D hole shapes.
    """
    class Meta:
        name = "ClassCatalogue_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    material_catalogue: List[MaterialCatalogue] = field(
        default_factory=list,
        metadata={
            "name": "MaterialCatalogue",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    xsection_catalogue: List[XsectionCatalogue] = field(
        default_factory=list,
        metadata={
            "name": "XSectionCatalogue",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    hole_shape_catalogue: List[HoleShapeCatalogue] = field(
        default_factory=list,
        metadata={
            "name": "HoleShapeCatalogue",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class CompartmentFace(CompartmentFaceT):
    """
    The face of a compartment defined by a surface boundary.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PlateT(StructurePartT):
    """
    Type definition of Structural concept of  plates used in shipbuilding.

    Attributes
        plate_material:
        offset: The material offset form the parent surface. A material
            offset is measured positive along the parent surface normal
            vector.
        outer_contour:
        unbounded_geometry:
        limited_by:
        inner_contour:
        cut_by: A structural concept defining a cut-out in a surface
            defined by a parametric hole or a set of generic trim
            curves. Cut-outs on plate will only remove material of the
            parent plate, no other parts.
        function_type:
    """
    class Meta:
        name = "Plate_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    plate_material: List[PlateMaterial] = field(
        default_factory=list,
        metadata={
            "name": "PlateMaterial",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    offset: List[Offset] = field(
        default_factory=list,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    outer_contour: List[OuterContour] = field(
        default_factory=list,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    unbounded_geometry: List[UnboundedGeometry] = field(
        default_factory=list,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    limited_by: List[LimitedBy] = field(
        default_factory=list,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    inner_contour: List[InnerContour] = field(
        default_factory=list,
        metadata={
            "name": "InnerContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cut_by: List[CutBy] = field(
        default_factory=list,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ReferenceSurfacesT:
    """
    Type definition of a collection of surfaces.
    """
    class Meta:
        name = "ReferenceSurfaces_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    plane3_d: List[Plane3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    nurbssurface: List[Nurbssurface] = field(
        default_factory=list,
        metadata={
            "name": "NURBSSurface",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    extruded_surface: List[ExtrudedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ExtrudedSurface",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    sphere3_d: List[Sphere3D] = field(
        default_factory=list,
        metadata={
            "name": "Sphere3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cone3_d: List[Cone3D] = field(
        default_factory=list,
        metadata={
            "name": "Cone3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cylinder3_d: List[Cylinder3D] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder3D",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    surface_collection: List[SurfaceCollection] = field(
        default_factory=list,
        metadata={
            "name": "SurfaceCollection",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Bracket(BracketT):
    """
    Structural concept of brackets used in shipbuilding.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ClassCatalogue(ClassCatalogueT):
    """The Class catalogues provided as part of the OCX.

    The catalogue can hold the society's definitions of cross sections,
    materials, hole shapes etc.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class CompartmentT(EntityBaseT):
    """
    Type definition of the  concept of a compartment part of the vessel capacity
    plan representing a closed volume (space) defined by  enclosing  structure
    panels.

    Attributes
        compartment_properties:
        compartment_face: The face of a compartment defined by a surface
            boundary. All faces must make up a a CLOSED volume defining
            the compartment.
        external_geometry_ref:
        bulk_cargo:
        liquid_cargo:
        unit_cargo:
        compartment_purpose:
    """
    class Meta:
        name = "Compartment_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    compartment_properties: Optional[CompartmentProperties] = field(
        default=None,
        metadata={
            "name": "CompartmentProperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    compartment_face: List[CompartmentFace] = field(
        default_factory=list,
        metadata={
            "name": "CompartmentFace",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    external_geometry_ref: Optional[ExternalGeometryRef] = field(
        default=None,
        metadata={
            "name": "ExternalGeometryRef",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bulk_cargo: List[BulkCargo] = field(
        default_factory=list,
        metadata={
            "name": "BulkCargo",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    liquid_cargo: List[LiquidCargo] = field(
        default_factory=list,
        metadata={
            "name": "LiquidCargo",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    unit_cargo: List[UnitCargo] = field(
        default_factory=list,
        metadata={
            "name": "UnitCargo",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    compartment_purpose: Optional[CompartmentPurposeValue] = field(
        default=None,
        metadata={
            "name": "compartmentPurpose",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Plate(PlateT):
    """
    Structural concept of plates used in shipbuilding.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ReferenceSurfaces(ReferenceSurfacesT):
    """
    Collection of frequently used surfaces which are referenced by more than one
    object.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Compartment(CompartmentT):
    """
    The concept of a compartment part of the vessel capacity plan representing a
    closed volume (space) defined by enclosing surface geometry.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class ComposedOfT:
    class Meta:
        name = "ComposedOf_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    plate: List[Plate] = field(
        default_factory=list,
        metadata={
            "name": "Plate",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "min_occurs": 1,
        }
    )
    bracket: List[Bracket] = field(
        default_factory=list,
        metadata={
            "name": "Bracket",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    pillar: List[Pillar] = field(
        default_factory=list,
        metadata={
            "name": "Pillar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ArrangementT(DescriptionBaseT):
    """
    Type definition of the vessel arrangement (of comparments).

    Attributes
        compartment: The  concept of a compartment part of the vessel
            arrangement  representing a CLOSED volume (space) defined by
            enclosing surface geometry.
        physical_space:
    """
    class Meta:
        name = "Arrangement_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    compartment: List[Compartment] = field(
        default_factory=list,
        metadata={
            "name": "Compartment",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    physical_space: List[PhysicalSpace] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalSpace",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class ComposedOf(ComposedOfT):
    """
    Element representing the structural concepts which composes a structure Panel.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class Arrangement(ArrangementT):
    """
    The vessel arrangement or capacity plan defined by its compartments.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class PanelT(EntityBaseT):
    """Type definition of Structural concept of shipbuilding panels.

    Panels can typically be composed of plates, seams and stiffeners.

    Attributes
        physical_properties:
        unbounded_geometry: The unbounded surface geometry of the parent
            element. Can be a patch of connected surfaces.
        limited_by:
        outer_contour:
        composed_of: The element representing the structural concepts
            which composes the structural Panel. If no ComposedOf
            definition is given, the Panel is treated as a virtual
            panel. A virtual panel is used to limit other objects
            defining the model topology.
        stiffened_by:
        split_by:
        cut_by: A structural concept defining a cut-out in a surface
            defined by a parametric hole or a set of generic trim
            curves. Cut-out on panels will cut material on all the panel
            plates touched by the cut-out shape.
        function_type:
        tightness:
    """
    class Meta:
        name = "Panel_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    physical_properties: Optional[PhysicalProperties] = field(
        default=None,
        metadata={
            "name": "PhysicalProperties",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    unbounded_geometry: Optional[UnboundedGeometry] = field(
        default=None,
        metadata={
            "name": "UnboundedGeometry",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    limited_by: Optional[LimitedBy] = field(
        default=None,
        metadata={
            "name": "LimitedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    outer_contour: Optional[OuterContour] = field(
        default=None,
        metadata={
            "name": "OuterContour",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    composed_of: Optional[ComposedOf] = field(
        default=None,
        metadata={
            "name": "ComposedOf",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    stiffened_by: Optional[StiffenedBy] = field(
        default=None,
        metadata={
            "name": "StiffenedBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    split_by: Optional[SplitBy] = field(
        default=None,
        metadata={
            "name": "SplitBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    cut_by: Optional[CutBy] = field(
        default=None,
        metadata={
            "name": "CutBy",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    function_type: Optional[FunctionTypeValue] = field(
        default=None,
        metadata={
            "name": "functionType",
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    tightness: Optional[TightnessValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )


@dataclass
class Panel(PanelT):
    """Structural concept of shipbuilding panels.

    Panels can typically be composed of plates, seams and stiffeners.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class VesselT(FormT):
    """
    Type definition of the Vessel asset subject to Classification.

    Attributes
        classification_data:
        builder_information:
        tonnage_data:
        statutory_data:
        ship_designation:
        coordinate_system: The vessel coordinate system definition. If
            not present, it is assumed that the Vessel is modelled in
            the global coordinate frame.
        design_view:
        arrangement:
        reference_surfaces: Collection of frequently used surfaces which
            are referenced by more than one object. Will typically
            contain th eouter shell definition.
        panel:
        plate:
        stiffener:
        bracket:
        pillar:
    """
    class Meta:
        name = "Vessel_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    classification_data: Optional[ClassificationData] = field(
        default=None,
        metadata={
            "name": "ClassificationData",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    builder_information: Optional[BuilderInformation] = field(
        default=None,
        metadata={
            "name": "BuilderInformation",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    tonnage_data: Optional[TonnageData] = field(
        default=None,
        metadata={
            "name": "TonnageData",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    statutory_data: Optional[StatutoryData] = field(
        default=None,
        metadata={
            "name": "StatutoryData",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    ship_designation: Optional[ShipDesignation] = field(
        default=None,
        metadata={
            "name": "ShipDesignation",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "CoordinateSystem",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
            "required": True,
        }
    )
    design_view: List[DesignView] = field(
        default_factory=list,
        metadata={
            "name": "DesignView",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    arrangement: List[Arrangement] = field(
        default_factory=list,
        metadata={
            "name": "Arrangement",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    reference_surfaces: List[ReferenceSurfaces] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceSurfaces",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    panel: List[Panel] = field(
        default_factory=list,
        metadata={
            "name": "Panel",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    plate: List[Plate] = field(
        default_factory=list,
        metadata={
            "name": "Plate",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    stiffener: List[Stiffener] = field(
        default_factory=list,
        metadata={
            "name": "Stiffener",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    bracket: List[Bracket] = field(
        default_factory=list,
        metadata={
            "name": "Bracket",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    pillar: List[Pillar] = field(
        default_factory=list,
        metadata={
            "name": "Pillar",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )


@dataclass
class Vessel(VesselT):
    """
    Vessel asset subject to Classification.
    """
    class Meta:
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"


@dataclass
class OcxXmlT(DocumentBaseT):
    """
    Root type of the schema.

    Attributes
        vessel:
        equipment:
        class_catalogue: The Class catalogues provided as part of the
            OCX. The catalogue can hold the society's definitions of
            cross sections, materials, hole shapes etc.
        units_ml:
    """
    class Meta:
        name = "ocxXML_T"
        target_namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"

    vessel: List[Vessel] = field(
        default_factory=list,
        metadata={
            "name": "Vessel",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    equipment: List[Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    class_catalogue: List[ClassCatalogue] = field(
        default_factory=list,
        metadata={
            "name": "ClassCatalogue",
            "type": "Element",
            "namespace": "http://data.dnvgl.com/Schemas/ocxXMLSchema",
        }
    )
    units_ml: List[UnitsMl] = field(
        default_factory=list,
        metadata={
            "name": "UnitsML",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
        }
    )


@dataclass
class OcxXml(OcxXmlT):
    """
    Root element of the schema.
    """
    class Meta:
        name = "ocxXML"
        namespace = "http://data.dnvgl.com/Schemas/ocxXMLSchema"
