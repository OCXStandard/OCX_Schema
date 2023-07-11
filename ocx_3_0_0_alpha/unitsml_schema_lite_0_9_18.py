from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from ocx_3_0_0_alpha.xml import LangValue

__NAMESPACE__ = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class AmountOfSubstanceType:
    """
    Type of the quantity amount of substance.

    Attributes
        symbol: Symbol of the quantity amount of substance.
        power_numerator: An integer exponent of the unit.
    """
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
    type_value: Optional[object] = field(
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
class Length(LengthType):
    """
    Element containing the dimension of the quantity length.
    """
    class Meta:
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
    length: List[Length] = field(
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
    enumerated_root_unit: List[EnumeratedRootUnit] = field(
        default_factory=list,
        metadata={
            "name": "EnumeratedRootUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18",
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
class Unit(UnitType):
    """Element for describing units.

    Use in containers UnitSet or directly incorporate into a host
    schema.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class UnitSetType:
    """
    Type for the unit container.

    Attributes
        unit: Element for describing units. Use in containers UnitSet or
            directly incorporate into a host schema.
    """
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
class UnitSet(UnitSetType):
    """Container for units.

    Use in UnitsML container or directly incorporate into a host schema.
    """
    class Meta:
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"


@dataclass
class UnitsMltype:
    """
    ComplexType for the root element of an UnitsML document.
    """
    class Meta:
        name = "UnitsMLType"

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
class UnitsMl(UnitsMltype):
    """
    Container for UnitsML units, quantities, and prefixes.
    """
    class Meta:
        name = "UnitsML"
        namespace = "urn:oasis:names:tc:unitsml:schema:xsd:UnitsMLSchema_lite-0.9.18"
