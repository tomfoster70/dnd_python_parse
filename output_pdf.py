import sys
import time
try:
    from fdfgen import forge_fdf
except:
    print("Hello! Thanks for giving me a go but I still need fdfgen.\nPlease see the read me.\nAlso are you using python2? because thats what I used for all the testing")
    time.sleep(10)
    sys.exit(1)

import xml.etree.ElementTree as ET
import re
import os
import math
import binascii
import traceback

mainDict =  { 'CharacterName 2'  :  '', 'Age'  :  '', 'Height'  :  '', 'Weight'  :  '', 'Eyes'  :  '',
      'Skin'  :  '', 'Hair'  :  '', 'Allies'  :  '', 'FactionName'  :  '', 'Backstory'  :  '',
      'Feat+Traits'  :  '', 'Treasure'  :  '', 'ClassLevel'  :  '', 'Background'  :  '',
      'PlayerName'  :  '', 'CharacterName'  :  '', 'Race '  :  '', 'Alignment'  :  '',
      'XP'  :  '', 'Inspiration'  :  '', 'STR'  :  '', 'ProfBonus'  :  '', 'AC'  :  '',
      'Initiative'  :  '', 'Speed'  :  '', 'PersonalityTraits '  :  '', 'STRmod'  :  '',
      'HPMax'  :  '', 'ST Strength'  :  '', 'DEX'  :  '', 'HPCurrent'  :  '', 'Ideals'  :  '',
      'DEXmod '  :  '', 'HPTemp'  :  '', 'Bonds'  :  '', 'CON'  :  '', 'HDTotal'  :  '',
      'Check Box 12'  :  False, 'Check Box 13'  :  False, 'Check Box 14'  :  False,
      'CONmod'  :  '', 'Check Box 15'  :  False, 'Check Box 16'  :  False,
      'Check Box 17'  :  False, 'HD'  :  '', 'Flaws'  :  '', 'INT'  :  '',
      'ST Dexterity'  :  '', 'ST Constitution'  :  '', 'ST Intelligence'  :  '',
      'ST Wisdom'  :  '', 'ST Charisma'  :  '', 'Acrobatics'  :  '', 'Animal'  :  '',
      'Athletics'  :  '', 'Deception '  :  '', 'History '  :  '', 'Insight'  :  '',
      'Intimidation'  :  '', 'Check Box 11'  :  False, 'Check Box 18'  :  False,
      'Check Box 19'  :  False, 'Check Box 20'  :  False, 'Check Box 21'  :  False,
      'Check Box 22'  :  False, 'Wpn Name'  :  '', 'Wpn1 AtkBonus'  :  '', 'Wpn1 Damage'  :  '',
      'INTmod'  :  '', 'Wpn Name 2'  :  '', 'Wpn2 AtkBonus '  :  '', 'Wpn2 Damage '  :  '',
      'Investigation '  :  '', 'WIS'  :  '', 'Wpn Name 3'  :  '', 'Wpn3 AtkBonus  '  :  '',
      'Arcana'  :  '', 'Wpn3 Damage '  :  '', 'Perception '  :  '', 'WISmod'  :  '', 'CHA'  :  '',
      'Nature'  :  '', 'Performance'  :  '', 'Medicine'  :  '', 'Religion'  :  '', 'Stealth '  :  '',
      'Check Box 23'  :  False, 'Check Box 24'  :  False, 'Check Box 25'  :  False,
      'Check Box 26'  :  False, 'Check Box 27'  :  False, 'Check Box 28'  :  False,
      'Check Box 29'  :  False, 'Check Box 30'  :  False, 'Check Box 31'  :  False,
      'Check Box 32'  :  False, 'Check Box 33'  :  False, 'Check Box 34'  :  False,
      'Check Box 35'  :  False, 'Check Box 36'  :  False, 'Check Box 37'  :  False,
      'Check Box 38'  :  False, 'Check Box 39'  :  False, 'Check Box 40'  :  False,
      'Persuasion'  :  '', 'SleightofHand'  :  '', 'CHamod'  :  '', 'Survival'  :  '',
      'AttacksSpellcasting'  :  '', 'Passive'  :  '', 'CP'  :  '', 'ProficienciesLang'  :  '',
      'SP'  :  '', 'EP'  :  '', 'GP'  :  '', 'PP'  :  '', 'Equipment'  :  '', 'Features and Traits'  :  '',
      'Spellcasting Class 2'  :  '', 'SpellcastingAbility 2'  :  '', 'SpellSaveDC  2'  :  '',
      'SpellAtkBonus 2'  :  '', 'SlotsTotal 19'  :  '', 'SlotsRemaining 19'  :  '', 'Spells 1014'  :  '',
      'Spells 1015'  :  '', 'Spells 1016'  :  '', 'Spells 1017'  :  '', 'Spells 1018'  :  '',
      'Spells 1019'  :  '', 'Spells 1020'  :  '', 'Spells 1021'  :  '', 'Spells 1022'  :  '',
      'Check Box 314'  :  False, 'Check Box 3031'  :  False, 'Check Box 3032'  :  False,
      'Check Box 3033'  :  False, 'Check Box 3034'  :  False, 'Check Box 3035'  :  False,
      'Check Box 3036'  :  False, 'Check Box 3037'  :  False, 'Check Box 3038'  :  False,
      'Check Box 3039'  :  False, 'Check Box 3040'  :  False, 'Check Box 321'  :  False,
      'Check Box 320'  :  False, 'Check Box 3060'  :  False, 'Check Box 3061'  :  False,
      'Check Box 3062'  :  False, 'Check Box 3063'  :  False, 'Check Box 3064'  :  False,
      'Check Box 3065'  :  False, 'Check Box 3066'  :  False, 'Check Box 315'  :  False,
      'Check Box 3041'  :  False, 'Spells 1023'  :  '', 'Check Box 251'  :  False,
      'Check Box 309'  :  False, 'Check Box 3010'  :  False, 'Check Box 3011'  :  False,
      'Check Box 3012'  :  False, 'Check Box 3013'  :  False, 'Check Box 3014'  :  False,
      'Check Box 3015'  :  False, 'Check Box 3016'  :  False, 'Check Box 3017'  :  False,
      'Check Box 3018'  :  False, 'Check Box 3019'  :  False, 'Spells 1024'  :  '',
      'Spells 1025'  :  '', 'Spells 1026'  :  '', 'Spells 1027'  :  '', 'Spells 1028'  :  '',
      'Spells 1029'  :  '', 'Spells 1030'  :  '', 'Spells 1031'  :  '', 'Spells 1032'  :  '',
      'Spells 1033'  :  '', 'SlotsTotal 20'  :  '', 'SlotsRemaining 20'  :  '', 'Spells 1034'  :  '',
      'Spells 1035'  :  '', 'Spells 1036'  :  '', 'Spells 1037'  :  '', 'Spells 1038'  :  '', 'Spells 1039'  :  '',
      'Spells 1040'  :  '', 'Spells 1041'  :  '', 'Spells 1042'  :  '', 'Spells 1043'  :  '', 'Spells 1044'  :  '',
      'Spells 1045'  :  '', 'Spells 1046'  :  '', 'SlotsTotal 21'  :  '', 'SlotsRemaining 21'  :  '', 'Spells 1047'  :  '',
      'Spells 1048'  :  '', 'Spells 1049'  :  '', 'Spells 1050'  :  '', 'Spells 1051'  :  '', 'Spells 1052'  :  '',
      'Spells 1053'  :  '', 'Spells 1054'  :  '', 'Spells 1055'  :  '', 'Spells 1056'  :  '', 'Spells 1057'  :  '',
      'Spells 1058'  :  '', 'Spells 1059'  :  '', 'SlotsTotal 22'  :  '', 'SlotsRemaining 22'  :  '',
      'Spells 1060'  :  '', 'Spells 1061'  :  '', 'Spells 1062'  :  '', 'Spells 1063'  :  '', 'Spells 1064'  :  '',
      'Check Box 323'  :  False, 'Check Box 322'  :  False, 'Check Box 3067'  :  False, 'Check Box 3068'  :  False,
      'Check Box 3069'  :  False, 'Check Box 3070'  :  False, 'Check Box 3071'  :  False,
      'Check Box 3072'  :  False, 'Check Box 3073'  :  False, 'Spells 1065'  :  '', 'Spells 1066'  :  '',
      'Spells 1067'  :  '', 'Spells 1068'  :  '', 'Spells 1069'  :  '', 'Spells 1070'  :  '', 'Spells 1071'  :  '',
      'Check Box 317'  :  False, 'Spells 1072'  :  '', 'SlotsTotal 23'  :  '', 'SlotsRemaining 23'  :  '',
      'Spells 1073'  :  '', 'Spells 1074'  :  '', 'Spells 1075'  :  '', 'Spells 1076'  :  '', 'Spells 1077'  :  '',
      'Spells 1078'  :  '', 'Spells 1079'  :  '', 'Spells 1080'  :  '', 'Spells 1081'  :  '', 'SlotsTotal 24'  :  '',
      'SlotsRemaining 24'  :  '', 'Spells 1082'  :  '', 'Spells 1083'  :  '', 'Spells 1084'  :  '', 'Spells 1085'  :  '',
      'Spells 1086'  :  '', 'Spells 1087'  :  '', 'Spells 1088'  :  '', 'Spells 1089'  :  '', 'Spells 1090'  :  '',
      'SlotsTotal 25'  :  '', 'SlotsRemaining 25'  :  '', 'Spells 1091'  :  '', 'Spells 1092'  :  '',
      'Spells 1093'  :  '', 'Spells 1094'  :  '', 'Spells 1095'  :  '', 'Spells 1096'  :  '', 'Spells 1097'  :  '',
      'Spells 1098'  :  '', 'Spells 1099'  :  '', 'SlotsTotal 26'  :  '', 'SlotsRemaining 26'  :  '',
      'Spells 10100'  :  '', 'Spells 10101'  :  '', 'Spells 10102'  :  '', 'Spells 10103'  :  '',
      'Check Box 316'  :  False, 'Check Box 3042'  :  False, 'Check Box 3043'  :  False,
      'Check Box 3044'  :  False, 'Check Box 3045'  :  False, 'Check Box 3046'  :  False,
      'Check Box 3047'  :  False, 'Check Box 3048'  :  False, 'Check Box 3049'  :  False,
      'Check Box 3050'  :  False, 'Check Box 3051'  :  False, 'Check Box 3052'  :  False,
      'Spells 10104'  :  '', 'Check Box 325'  :  False, 'Check Box 324'  :  False,
      'Check Box 3074'  :  False, 'Check Box 3075'  :  False, 'Check Box 3076'  :  False,
      'Check Box 3077'  :  False, 'Spells 10105'  :  '', 'Spells 10106'  :  '', 'Check Box 3078'  :  False,
      'SlotsTotal 27'  :  '', 'SlotsRemaining 27'  :  '', 'Check Box 313'  :  False, 'Check Box 310'  :  False,
      'Check Box 3020'  :  False, 'Check Box 3021'  :  False, 'Check Box 3022'  :  False,
      'Check Box 3023'  :  False, 'Check Box 3024'  :  False, 'Check Box 3025'  :  False,
      'Check Box 3026'  :  False, 'Check Box 3027'  :  False, 'Check Box 3028'  :  False,
      'Check Box 3029'  :  False, 'Check Box 3030'  :  False, 'Spells 10107'  :  '',
      'Spells 10108'  :  '', 'Spells 10109'  :  '', 'Spells 101010'  :  '', 'Spells 101011'  :  '',
      'Spells 101012'  :  '', 'Check Box 319'  :  False, 'Check Box 318'  :  False,
      'Check Box 3053'  :  False, 'Check Box 3054'  :  False, 'Check Box 3055'  :  False,
      'Check Box 3056'  :  False, 'Check Box 3057'  :  False, 'Check Box 3058'  :  False,
      'Check Box 3059'  :  False, 'Check Box 327'  :  False, 'Check Box 326'  :  False,
      'Check Box 3079'  :  False, 'Check Box 3080'  :  False, 'Check Box 3081'  :  False,
      'Check Box 3082'  :  False, 'Spells 101013'  :  '', 'Check Box 3083' : False}

class AlternativeCharacterSheet:

    input_pdf = 'Character Sheet - Alternative - Form Fillable.pdf'
    output_name = 'Alternative'

    CHAMOD = 'CHamod'
    CHECK_BOX_3077 = 'Check Box 3077'
    CHECK_BOX_3029 = 'Check Box 3029'
    ST_CONSTITUTION = 'SavingThrows3'
    SPELLS_1015 = 'Spells 1015'
    ARCANA = 'Arcana'
    RELIGION = 'Religion'
    SPELLS_10105 = 'Spells 10105'
    CHECK_BOX_3075 = 'Check Box 3075'
    CHECK_BOX_3021 = 'Check Box 3021'
    ST_INTELLIGENCE = 'SavingThrows4'
    CHECK_BOX_3074 = 'Check Box 3074'
    SPELLS_1089 = 'Spells 1089'
    SPELLS_10100 = 'Spells 10100'
    HISTORY = 'History'
    SPELLS_1033 = 'Spells 1033'
    SPELLS_1030 = 'Spells 1030'
    SLEIGHTOFHAND = 'SleightofHand'
    SPELLS_1036 = 'Spells 1036'
    SPELLS_1037 = 'Spells 1037'
    SPELLS_1034 = 'Spells 1034'
    BONDS = 'Bonds'
    SPELLS_1038 = 'Spells 1038'
    SPELLS_1039 = 'Spells 1039'
    SPELLS_10107 = 'Spells 10107'
    SPELLS_1079 = 'Spells 1079'
    CHECK_BOX_3041 = 'Check Box 3041'
    SPELLS_1088 = 'Spells 1088'
    CHECK_BOX_3050 = 'Check Box 3050'
    CHECK_BOX_3053 = 'Check Box 3053'
    CHECK_BOX_3052 = 'Check Box 3052'
    CHECK_BOX_3055 = 'Check Box 3055'
    CHECK_BOX_3054 = 'Check Box 3054'
    CHECK_BOX_3057 = 'Check Box 3057'
    CHECK_BOX_3056 = 'Check Box 3056'
    CHECK_BOX_3059 = 'Check Box 3059'
    CHECK_BOX_3058 = 'Check Box 3058'
    CLASSLEVEL = 'ClassLevel'
    DEXMOD = 'DEXmod '
    SPELLS_1078 = 'Spells 1078'
    CHECK_BOX_309 = 'Check Box 309'
    CHECK_BOX_3031 = 'Check Box 3031'
    GP = 'GP'
    CHECK_BOX_3030 = 'Check Box 3030'
    WPN_NAME_2 = 'Wpn Name 2'
    WPN_NAME_3 = 'Wpn Name 3'
    STEALTH = 'Stealth'
    CHECK_BOX_3068 = 'Check Box 3068'
    ATHLETICS = 'Athletics'
    CHECK_BOX_3069 = 'Check Box 3069'
    RACE = 'Race '
    PASSIVE = 'Passive'
    SPELLS_1045 = 'Spells 1045'
    SPELLS_1044 = 'Spells 1044'
    SPELLS_1043 = 'Spells 1043'
    SPELLS_1042 = 'Spells 1042'
    SPELLS_1041 = 'Spells 1041'
    HPMAX = 'HPMax'
    CHECK_BOX_3064 = 'Check Box 3064'
    STRMOD = 'STRmod'
    CHECK_BOX_3066 = 'Check Box 3066'
    SPELLS_1040 = 'Spells 1040'
    CHECK_BOX_3060 = 'Check Box 3060'
    CHECK_BOX_3061 = 'Check Box 3061'
    CHECK_BOX_3062 = 'Check Box 3062'
    CHECK_BOX_3063 = 'Check Box 3063'
    L1_SLOTSTOTAL = 'SlotsTotal 19'
    SKIN = 'Skin'
    SPELLS_1047 = 'Spells 1047'
    SPELLS_1092 = 'Spells 1092'
    SPELLS_1048 = 'Spells 1048'
    HPTEMP = 'HPTemp'
    SPELLS_1076 = 'Spells 1076'
    DEX = 'DEX'
    CHECK_BOX_3067 = 'Check Box 3067'
    INSIGHT_PROF = 'ChBx Insight'
    SPELLS_1075 = 'Spells 1075'
    CHECK_BOX_319 = 'Check Box 319'
    CHECK_BOX_316 = 'Check Box 316'
    SURVIVAL_PROF = 'ChBx Survival'
    CHECK_BOX_314 = 'Check Box 314'
    TREASURE = 'Treasure'
    CHECK_BOX_313 = 'Check Box 313'
    CHECK_BOX_310 = 'Check Box 310'
    MEDICINE = 'Medicine'
    SPELLS_1049 = 'Spells 1049'
    SPELLS_1077 = 'Spells 1077'
    SLOTSREMAINING_20 = 'SlotsRemaining 20'
    PERFORMANCE = 'Performance'
    SLOTSREMAINING_22 = 'SlotsRemaining 22'
    ACROBATICS = 'Acrobatics'
    SLOTSREMAINING_24 = 'SlotsRemaining 24'
    SPELLS_1067 = 'Spells 1067'
    HD = 'HD'
    SLOTSREMAINING_27 = 'SlotsRemaining 27'
    SPELLS_1054 = 'Spells 1054'
    SPELLS_1055 = 'Spells 1055'
    PP = 'PP'
    INTMOD = 'INTmod'
    SPELLS_1050 = 'Spells 1050'
    SPELLS_1051 = 'Spells 1051'
    SPELLS_1052 = 'Spells 1052'
    SPELLS_1053 = 'Spells 1053'
    WPN3_ATKBONUS = 'Wpn3 AtkBonus  '
    BACKSTORY = 'Backstory'
    FACTIONNAME = 'FactionName'
    CHECK_BOX_3070 = 'Check Box 3070'
    SPELLS_1058 = 'Spells 1058'
    SPELLS_1059 = 'Spells 1059'
    WPN_NAME = 'Wpn Name'
    SPELLS_1073 = 'Spells 1073'
    SPELLS_1070 = 'Spells 1070'
    CHA = 'CHA'
    INVESTIGATION = 'Investigation'
    SPELLS_1074 = 'Spells 1074'
    INT_PROF_CHECK_BOX = 'ST Intelligence'
    CHECK_BOX_321 = 'Check Box 321'
    INSPIRATION = 'ProfBonus'
    SPELLS_1032 = 'Spells 1032'
    SPELLCASTING_CLASS_2 = 'Spellcasting Class 2'
    SPELLS_10103 = 'Spells 10103'
    CHECK_BOX_323 = 'Check Box 323'
    CHECK_BOX_322 = 'Check Box 322'
    AGE = 'Age'
    ST_STRENGTH = 'SavingThrows'
    CHECK_BOX_327 = 'Check Box 327'
    WPN3_DAMAGE = 'Wpn3 Damage '
    CHECK_BOX_325 = 'Check Box 325'
    CHECK_BOX_324 = 'Check Box 324'
    SPELLS_1069 = 'Spells 1069'
    SPELLS_1068 = 'Spells 1068'
    SPELLS_1031 = 'Spells 1031'
    SLEIGHTOFHAND_PROF = 'ChBx Sleightofhand'
    STEALTH_PROF = 'ChBx Stealth'
    SPELLS_1046 = 'Spells 1046'
    PERCEPTION_PROF = 'ChBx Perception'
    PERFORMANCE_PROF = 'ChBx Performance'
    PERSUASION_PROF = 'ChBx Persuasion'
    RELIGION_PROF = 'ChBx Religion'
    INTIMIDATION_PROF = 'ChBx Intimidation'
    INVESTIGATION_PROF = 'ChBx Investigation'
    MEDICINE_PROF = 'ChBx Medicine'
    NATURE_PROF = 'ChBx Nature'
    CHECK_BOX_3065 = 'Check Box 3065'
    CHECK_BOX_3023 = 'Check Box 3023'
    SPELLS_10102 = 'Spells 10102'
    CHECK_BOX_3076 = 'Check Box 3076'
    WEIGHT = 'Weight'
    CHECK_BOX_3079 = 'Check Box 3079'
    INT = 'INT'
    SPELLS_1035 = 'Spells 1035'
    SPELLS_1081 = 'Spells 1081'
    INSIGHT = 'Insight'
    SPELLS_10101 = 'Spells 10101'
    CHECK_BOX_3047 = 'Check Box 3047'
    CONMOD = 'CONmod'
    CHECK_BOX_3025 = 'Check Box 3025'
    HAIR = 'Hair'
    CHECK_BOX_3080 = 'Check Box 3080'
    SPELLS_101010 = 'Spells 101010'
    SPELLS_101011 = 'Spells 101011'
    CHECK_BOX_3026 = 'Check Box 3026'
    SPELLS_1072 = 'Spells 1072'
    SPELLS_101012 = 'Spells 101012'
    ST_DEXTERITY = 'SavingThrows2'
    CHECK_BOX_3027 = 'Check Box 3027'
    ALIGNMENT = 'Alignment'
    CHECK_BOX_3020 = 'Check Box 3020'
    FLAWS = 'Flaws'
    HPCURRENT = 'HPCurrent'
    CHARACTERNAME = 'CharacterName'
    SPELLS_1060 = 'Spells 1060'
    CHECK_BOX_3081 = 'Check Box 3081'
    FEAT_TRAITS = 'Feat+Traits'
    SLOTSREMAINING_25 = 'SlotsRemaining 25'
    SPELLS_1061 = 'Spells 1061'
    WPN2_ATKBONUS = 'Wpn2 AtkBonus '
    ANIMAL = 'Animal Handling'
    HISTORY_PROF = 'ChBx History'
    WPN2_DAMAGE = 'Wpn2 Damage '
    ATHLETICS_PROF = 'ChBx athletics'
    ARCANA_PROF = 'ChBx Arcana'
    ANIMAL_PROF = 'ChBx Animal'
    ACROBATICS_PROF = 'ChBx Acrobatics'
    CHA_PROF_CHECK_BOX = 'ST Charisma'
    WIS_PROF_CHECK_BOX = 'ST Wisdom'
    CON = 'CON'
    CHECK_BOX_3051 = 'Check Box 3051'
    SPELLS_1062 = 'Spells 1062'
    CHECK_BOX_318 = 'Check Box 318'
    NATURE = 'Nature'
    SPELLS_1063 = 'Spells 1063'
    SPELLATKBONUS_2 = 'SpellAtkBonus 2'
    CHECK_BOX_3024 = 'Check Box 3024'
    SLOTSREMAINING_26 = 'SlotsRemaining 26'
    EP = 'EP'
    SPELLS_1066 = 'Spells 1066'
    CP = 'CP'
    HDTOTAL = 'HDTotal'
    CHECK_BOX_317 = 'Check Box 317'
    CHECK_BOX_3015 = 'Check Box 3015'
    CHECK_BOX_3014 = 'Check Box 3014'
    CHECK_BOX_3017 = 'Check Box 3017'
    CHECK_BOX_3016 = 'Check Box 3016'
    CHECK_BOX_3011 = 'Check Box 3011'
    CHECK_BOX_3010 = 'Check Box 3010'
    DECEPTION_PROF = 'ChBx deception'
    CHECK_BOX_3012 = 'Check Box 3012'
    SPELLSAVEDC__2 = 'SpellSaveDC  2'
    CHECK_BOX_315 = 'Check Box 315'
    ALLIES = 'Allies'
    SPELLS_1095 = 'Spells 1095'
    CHECK_BOX_3082 = 'Check Box 3082'
    DECEPTION = 'Deception'
    SPELLS_1071 = 'Spells 1071'
    SPELLS_1082 = 'Spells 1082'
    DEX_PROF_CHECK_BOX = 'ST Dexterity'
    CON_PROF_CHECK_BOX = 'ST Constitution'
    SPELLS_1087 = 'Spells 1087'
    SPELLS_1086 = 'Spells 1086'
    SPELLS_1085 = 'Spells 1085'
    SPELLS_1084 = 'Spells 1084'
    DEATH_SAVE_SUCCESS_1 = 'Check Box 12'
    DEATH_SAVE_SUCCESS_2 = 'Check Box 13'
    XP = 'XP'
    STR_PROF_CHECK_BOX = 'ST Strength'
    DEATH_SAVE_FAIL_2 = 'Check Box 16'
    DEATH_SAVE_FAIL_3 = 'Check Box 17'
    DEATH_SAVE_SUCCESS_3 = 'Check Box 14'
    DEATH_SAVE_FAIL_1 = 'Check Box 15'
    SPELLS_1090 = 'Spells 1090'
    WPN1_ATKBONUS = 'Wpn1 AtkBonus'
    SPELLCASTINGABILITY_2 = 'SpellcastingAbility 2'
    EQUIPMENT = 'Equipment'
    SP = 'SP'
    PERSUASION = 'Persuasion'
    HEIGHT = 'Height'
    CHECK_BOX_3028 = 'Check Box 3028'
    SPELLS_1065 = 'Spells 1065'
    SPELLS_10106 = 'Spells 10106'
    INITIATIVE = 'Initiative'
    CHECK_BOX_3013 = 'Check Box 3013'
    SLOTSTOTAL_22 = 'SlotsTotal 22'
    SLOTSTOTAL_23 = 'SlotsTotal 23'
    SLOTSTOTAL_20 = 'SlotsTotal 20'
    SLOTSTOTAL_21 = 'SlotsTotal 21'
    SLOTSTOTAL_26 = 'SlotsTotal 26'
    SLOTSTOTAL_27 = 'SlotsTotal 27'
    SLOTSTOTAL_24 = 'SlotsTotal 24'
    SLOTSTOTAL_25 = 'SlotsTotal 25'
    SPELLS_1080 = 'Spells 1080'
    SPELLS_1064 = 'Spells 1064'
    SPELLS_1096 = 'Spells 1096'
    WISMOD = 'WISmod'
    SPELLS_1097 = 'Spells 1097'
    CHECK_BOX_3078 = 'Check Box 3078'
    PERCEPTION = 'Perception'
    SPELLS_1091 = 'Spells 1091'
    CHECK_BOX_3018 = 'Check Box 3018'
    SPELLS_1093 = 'Spells 1093'
    SPELLS_1094 = 'Spells 1094'
    SPELLS_1023 = 'Spells 1023'
    CHECK_BOX_320 = 'Check Box 320'
    CHECK_BOX_3019 = 'Check Box 3019'
    SPELLS_1098 = 'Spells 1098'
    WIS = 'WIS'
    ST_WISDOM = 'SavingThrows5'
    SPELLS_10109 = 'Spells 10109'
    SPELLS_10108 = 'Spells 10108'
    SPELLS_1018 = 'Spells 1018'
    IDEALS = 'Ideals'
    EYES = 'Eyes'
    SLOTSREMAINING_23 = 'SlotsRemaining 23'
    CHECK_BOX_3043 = 'Check Box 3043'
    SURVIVAL = 'Survival'
    SPELLS_1014 = 'Spells 1014'
    INTIMIDATION = 'Intimidation'
    SPELLS_1016 = 'Spells 1016'
    SPELLS_1017 = 'Spells 1017'
    CHECK_BOX_3037 = 'Check Box 3037'
    CHECK_BOX_3036 = 'Check Box 3036'
    CHECK_BOX_3035 = 'Check Box 3035'
    CHECK_BOX_3034 = 'Check Box 3034'
    CHECK_BOX_3033 = 'Check Box 3033'
    CHECK_BOX_3032 = 'Check Box 3032'
    BACKGROUND = 'Background'
    PROFBONUS = 'Inspiration'
    CHARACTERNAME_2 = 'CharacterName 2'
    PROFICIENCIESLANG = 'ProficienciesLang'
    CHECK_BOX_3038 = 'Check Box 3038'
    SPELLS_1099 = 'Spells 1099'
    AC = 'AC'
    SPELLS_101013 = 'Spells 101013'
    SPELLS_1019 = 'Spells 1019'
    PLAYERNAME = 'PlayerName'
    SPELLS_10104 = 'Spells 10104'
    CHECK_BOX_3045 = 'Check Box 3045'
    SPELLS_1056 = 'Spells 1056'
    WPN1_DAMAGE = 'Wpn1 Damage'
    CHECK_BOX_326 = 'Check Box 326'
    SPELLS_1057 = 'Spells 1057'
    STR = 'STR'
    SLOTSREMAINING_19 = 'SlotsRemaining 19'
    ST_CHARISMA = 'SavingThrows6'
    CHECK_BOX_3022 = 'Check Box 3022'
    CHECK_BOX_3083 = 'Check Box 3083'
    SPELLS_1083 = 'Spells 1083'
    SPELLS_1029 = 'Spells 1029'
    SPELLS_1028 = 'Spells 1028'
    CHECK_BOX_3039 = 'Check Box 3039'
    SPELLS_1025 = 'Spells 1025'
    SPELLS_1024 = 'Spells 1024'
    SPELLS_1027 = 'Spells 1027'
    SPELLS_1026 = 'Spells 1026'
    SPELLS_1021 = 'Spells 1021'
    SPELLS_1020 = 'Spells 1020'
    FEATURES_AND_TRAITS = 'Features and Traits'
    SPELLS_1022 = 'Spells 1022'
    CHECK_BOX_3042 = 'Check Box 3042'
    CHECK_BOX_3073 = 'Check Box 3073'
    CHECK_BOX_3040 = 'Check Box 3040'
    PERSONALITYTRAITS = 'PersonalityTraits '
    CHECK_BOX_3046 = 'Check Box 3046'
    CHECK_BOX_251 = 'Check Box 251'
    CHECK_BOX_3044 = 'Check Box 3044'
    CHECK_BOX_3072 = 'Check Box 3072'
    ATTACKSSPELLCASTING = 'AttacksSpellcasting'
    CHECK_BOX_3048 = 'Check Box 3048'
    CHECK_BOX_3049 = 'Check Box 3049'
    SPEED = 'Speed'
    CHECK_BOX_3071 = 'Check Box 3071'
    SLOTSREMAINING_21 = 'SlotsRemaining 21'


class CharacterSheet:

    input_pdf = 'DnD_5E_CharacterSheet - Form Fillable.pdf'
    output_name = 'Normal'

    CHAMOD = 'CHamod'
    CHECK_BOX_3077 = 'Check Box 3077'
    CHECK_BOX_3029 = 'Check Box 3029'
    ST_CONSTITUTION = 'ST Constitution'
    SPELLS_1015 = 'Spells 1015'
    ARCANA = 'Arcana'
    RELIGION = 'Religion'
    SPELLS_10105 = 'Spells 10105'
    CHECK_BOX_3075 = 'Check Box 3075'
    CHECK_BOX_3021 = 'Check Box 3021'
    ST_INTELLIGENCE = 'ST Intelligence'
    CHECK_BOX_3074 = 'Check Box 3074'
    SPELLS_1089 = 'Spells 1089'
    SPELLS_10100 = 'Spells 10100'
    HISTORY = 'History '
    SPELLS_1033 = 'Spells 1033'
    SPELLS_1030 = 'Spells 1030'
    SLEIGHTOFHAND = 'SleightofHand'
    SPELLS_1036 = 'Spells 1036'
    SPELLS_1037 = 'Spells 1037'
    SPELLS_1034 = 'Spells 1034'
    BONDS = 'Bonds'
    SPELLS_1038 = 'Spells 1038'
    SPELLS_1039 = 'Spells 1039'
    SPELLS_10107 = 'Spells 10107'
    SPELLS_1079 = 'Spells 1079'
    CHECK_BOX_3041 = 'Check Box 3041'
    SPELLS_1088 = 'Spells 1088'
    CHECK_BOX_3050 = 'Check Box 3050'
    CHECK_BOX_3053 = 'Check Box 3053'
    CHECK_BOX_3052 = 'Check Box 3052'
    CHECK_BOX_3055 = 'Check Box 3055'
    CHECK_BOX_3054 = 'Check Box 3054'
    CHECK_BOX_3057 = 'Check Box 3057'
    CHECK_BOX_3056 = 'Check Box 3056'
    CHECK_BOX_3059 = 'Check Box 3059'
    CHECK_BOX_3058 = 'Check Box 3058'
    CLASSLEVEL = 'ClassLevel'
    DEXMOD = 'DEXmod '
    SPELLS_1078 = 'Spells 1078'
    CHECK_BOX_309 = 'Check Box 309'
    CHECK_BOX_3031 = 'Check Box 3031'
    GP = 'GP'
    CHECK_BOX_3030 = 'Check Box 3030'
    WPN_NAME_2 = 'Wpn Name 2'
    WPN_NAME_3 = 'Wpn Name 3'
    STEALTH = 'Stealth '
    CHECK_BOX_3068 = 'Check Box 3068'
    ATHLETICS = 'Athletics'
    CHECK_BOX_3069 = 'Check Box 3069'
    RACE = 'Race '
    PASSIVE = 'Passive'
    SPELLS_1045 = 'Spells 1045'
    SPELLS_1044 = 'Spells 1044'
    SPELLS_1043 = 'Spells 1043'
    SPELLS_1042 = 'Spells 1042'
    SPELLS_1041 = 'Spells 1041'
    HPMAX = 'HPMax'
    CHECK_BOX_3064 = 'Check Box 3064'
    STRMOD = 'STRmod'
    CHECK_BOX_3066 = 'Check Box 3066'
    SPELLS_1040 = 'Spells 1040'
    CHECK_BOX_3060 = 'Check Box 3060'
    CHECK_BOX_3061 = 'Check Box 3061'
    CHECK_BOX_3062 = 'Check Box 3062'
    CHECK_BOX_3063 = 'Check Box 3063'
    L1_SLOTSTOTAL = 'SlotsTotal 19'
    SKIN = 'Skin'
    SPELLS_1047 = 'Spells 1047'
    SPELLS_1092 = 'Spells 1092'
    SPELLS_1048 = 'Spells 1048'
    HPTEMP = 'HPTemp'
    SPELLS_1076 = 'Spells 1076'
    DEX = 'DEX'
    CHECK_BOX_3067 = 'Check Box 3067'
    INSIGHT_PROF = 'Check Box 29'
    SPELLS_1075 = 'Spells 1075'
    CHECK_BOX_319 = 'Check Box 319'
    CHECK_BOX_316 = 'Check Box 316'
    SURVIVAL_PROF = 'Check Box 40'
    CHECK_BOX_314 = 'Check Box 314'
    TREASURE = 'Treasure'
    CHECK_BOX_313 = 'Check Box 313'
    CHECK_BOX_310 = 'Check Box 310'
    MEDICINE = 'Medicine'
    SPELLS_1049 = 'Spells 1049'
    SPELLS_1077 = 'Spells 1077'
    SLOTSREMAINING_20 = 'SlotsRemaining 20'
    PERFORMANCE = 'Performance'
    SLOTSREMAINING_22 = 'SlotsRemaining 22'
    ACROBATICS = 'Acrobatics'
    SLOTSREMAINING_24 = 'SlotsRemaining 24'
    SPELLS_1067 = 'Spells 1067'
    HD = 'HD'
    SLOTSREMAINING_27 = 'SlotsRemaining 27'
    SPELLS_1054 = 'Spells 1054'
    SPELLS_1055 = 'Spells 1055'
    PP = 'PP'
    INTMOD = 'INTmod'
    SPELLS_1050 = 'Spells 1050'
    SPELLS_1051 = 'Spells 1051'
    SPELLS_1052 = 'Spells 1052'
    SPELLS_1053 = 'Spells 1053'
    WPN3_ATKBONUS = 'Wpn3 AtkBonus  '
    BACKSTORY = 'Backstory'
    FACTIONNAME = 'FactionName'
    CHECK_BOX_3070 = 'Check Box 3070'
    SPELLS_1058 = 'Spells 1058'
    SPELLS_1059 = 'Spells 1059'
    WPN_NAME = 'Wpn Name'
    SPELLS_1073 = 'Spells 1073'
    SPELLS_1070 = 'Spells 1070'
    CHA = 'CHA'
    INVESTIGATION = 'Investigation '
    SPELLS_1074 = 'Spells 1074'
    INT_PROF_CHECK_BOX = 'Check Box 20'
    CHECK_BOX_321 = 'Check Box 321'
    INSPIRATION = 'Inspiration'
    SPELLS_1032 = 'Spells 1032'
    SPELLCASTING_CLASS_2 = 'Spellcasting Class 2'
    SPELLS_10103 = 'Spells 10103'
    CHECK_BOX_323 = 'Check Box 323'
    CHECK_BOX_322 = 'Check Box 322'
    AGE = 'Age'
    ST_STRENGTH = 'ST Strength'
    CHECK_BOX_327 = 'Check Box 327'
    WPN3_DAMAGE = 'Wpn3 Damage '
    CHECK_BOX_325 = 'Check Box 325'
    CHECK_BOX_324 = 'Check Box 324'
    SPELLS_1069 = 'Spells 1069'
    SPELLS_1068 = 'Spells 1068'
    SPELLS_1031 = 'Spells 1031'
    SLEIGHTOFHAND_PROF = 'Check Box 38'
    STEALTH_PROF = 'Check Box 39'
    SPELLS_1046 = 'Spells 1046'
    PERCEPTION_PROF = 'Check Box 34'
    PERFORMANCE_PROF = 'Check Box 35'
    PERSUASION_PROF = 'Check Box 36'
    RELIGION_PROF = 'Check Box 37'
    INTIMIDATION_PROF = 'Check Box 30'
    INVESTIGATION_PROF = 'Check Box 31'
    MEDICINE_PROF = 'Check Box 32'
    NATURE_PROF = 'Check Box 33'
    CHECK_BOX_3065 = 'Check Box 3065'
    CHECK_BOX_3023 = 'Check Box 3023'
    SPELLS_10102 = 'Spells 10102'
    CHECK_BOX_3076 = 'Check Box 3076'
    WEIGHT = 'Weight'
    CHECK_BOX_3079 = 'Check Box 3079'
    INT = 'INT'
    SPELLS_1035 = 'Spells 1035'
    SPELLS_1081 = 'Spells 1081'
    INSIGHT = 'Insight'
    SPELLS_10101 = 'Spells 10101'
    CHECK_BOX_3047 = 'Check Box 3047'
    CONMOD = 'CONmod'
    CHECK_BOX_3025 = 'Check Box 3025'
    HAIR = 'Hair'
    CHECK_BOX_3080 = 'Check Box 3080'
    SPELLS_101010 = 'Spells 101010'
    SPELLS_101011 = 'Spells 101011'
    CHECK_BOX_3026 = 'Check Box 3026'
    SPELLS_1072 = 'Spells 1072'
    SPELLS_101012 = 'Spells 101012'
    ST_DEXTERITY = 'ST Dexterity'
    CHECK_BOX_3027 = 'Check Box 3027'
    ALIGNMENT = 'Alignment'
    CHECK_BOX_3020 = 'Check Box 3020'
    FLAWS = 'Flaws'
    HPCURRENT = 'HPCurrent'
    CHARACTERNAME = 'CharacterName'
    SPELLS_1060 = 'Spells 1060'
    CHECK_BOX_3081 = 'Check Box 3081'
    FEAT_TRAITS = 'Feat+Traits'
    SLOTSREMAINING_25 = 'SlotsRemaining 25'
    SPELLS_1061 = 'Spells 1061'
    WPN2_ATKBONUS = 'Wpn2 AtkBonus '
    ANIMAL = 'Animal'
    HISTORY_PROF = 'Check Box 28'
    WPN2_DAMAGE = 'Wpn2 Damage '
    ATHLETICS_PROF = 'Check Box 26'
    ARCANA_PROF = 'Check Box 25'
    ANIMAL_PROF = 'Check Box 24'
    ACROBATICS_PROF = 'Check Box 23'
    CHA_PROF_CHECK_BOX = 'Check Box 22'
    WIS_PROF_CHECK_BOX = 'Check Box 21'
    CON = 'CON'
    CHECK_BOX_3051 = 'Check Box 3051'
    SPELLS_1062 = 'Spells 1062'
    CHECK_BOX_318 = 'Check Box 318'
    NATURE = 'Nature'
    SPELLS_1063 = 'Spells 1063'
    SPELLATKBONUS_2 = 'SpellAtkBonus 2'
    CHECK_BOX_3024 = 'Check Box 3024'
    SLOTSREMAINING_26 = 'SlotsRemaining 26'
    EP = 'EP'
    SPELLS_1066 = 'Spells 1066'
    CP = 'CP'
    HDTOTAL = 'HDTotal'
    CHECK_BOX_317 = 'Check Box 317'
    CHECK_BOX_3015 = 'Check Box 3015'
    CHECK_BOX_3014 = 'Check Box 3014'
    CHECK_BOX_3017 = 'Check Box 3017'
    CHECK_BOX_3016 = 'Check Box 3016'
    CHECK_BOX_3011 = 'Check Box 3011'
    CHECK_BOX_3010 = 'Check Box 3010'
    DECEPTION_PROF = 'Check Box 27'
    CHECK_BOX_3012 = 'Check Box 3012'
    SPELLSAVEDC__2 = 'SpellSaveDC  2'
    CHECK_BOX_315 = 'Check Box 315'
    ALLIES = 'Allies'
    SPELLS_1095 = 'Spells 1095'
    CHECK_BOX_3082 = 'Check Box 3082'
    DECEPTION = 'Deception '
    SPELLS_1071 = 'Spells 1071'
    SPELLS_1082 = 'Spells 1082'
    DEX_PROF_CHECK_BOX = 'Check Box 18'
    CON_PROF_CHECK_BOX = 'Check Box 19'
    SPELLS_1087 = 'Spells 1087'
    SPELLS_1086 = 'Spells 1086'
    SPELLS_1085 = 'Spells 1085'
    SPELLS_1084 = 'Spells 1084'
    DEATH_SAVE_SUCCESS_1 = 'Check Box 12'
    DEATH_SAVE_SUCCESS_2 = 'Check Box 13'
    XP = 'XP'
    STR_PROF_CHECK_BOX = 'Check Box 11'
    DEATH_SAVE_FAIL_2 = 'Check Box 16'
    DEATH_SAVE_FAIL_3 = 'Check Box 17'
    DEATH_SAVE_SUCCESS_3 = 'Check Box 14'
    DEATH_SAVE_FAIL_1 = 'Check Box 15'
    SPELLS_1090 = 'Spells 1090'
    WPN1_ATKBONUS = 'Wpn1 AtkBonus'
    SPELLCASTINGABILITY_2 = 'SpellcastingAbility 2'
    EQUIPMENT = 'Equipment'
    SP = 'SP'
    PERSUASION = 'Persuasion'
    HEIGHT = 'Height'
    CHECK_BOX_3028 = 'Check Box 3028'
    SPELLS_1065 = 'Spells 1065'
    SPELLS_10106 = 'Spells 10106'
    INITIATIVE = 'Initiative'
    CHECK_BOX_3013 = 'Check Box 3013'
    SLOTSTOTAL_22 = 'SlotsTotal 22'
    SLOTSTOTAL_23 = 'SlotsTotal 23'
    SLOTSTOTAL_20 = 'SlotsTotal 20'
    SLOTSTOTAL_21 = 'SlotsTotal 21'
    SLOTSTOTAL_26 = 'SlotsTotal 26'
    SLOTSTOTAL_27 = 'SlotsTotal 27'
    SLOTSTOTAL_24 = 'SlotsTotal 24'
    SLOTSTOTAL_25 = 'SlotsTotal 25'
    SPELLS_1080 = 'Spells 1080'
    SPELLS_1064 = 'Spells 1064'
    SPELLS_1096 = 'Spells 1096'
    WISMOD = 'WISmod'
    SPELLS_1097 = 'Spells 1097'
    CHECK_BOX_3078 = 'Check Box 3078'
    PERCEPTION = 'Perception '
    SPELLS_1091 = 'Spells 1091'
    CHECK_BOX_3018 = 'Check Box 3018'
    SPELLS_1093 = 'Spells 1093'
    SPELLS_1094 = 'Spells 1094'
    SPELLS_1023 = 'Spells 1023'
    CHECK_BOX_320 = 'Check Box 320'
    CHECK_BOX_3019 = 'Check Box 3019'
    SPELLS_1098 = 'Spells 1098'
    WIS = 'WIS'
    ST_WISDOM = 'ST Wisdom'
    SPELLS_10109 = 'Spells 10109'
    SPELLS_10108 = 'Spells 10108'
    SPELLS_1018 = 'Spells 1018'
    IDEALS = 'Ideals'
    EYES = 'Eyes'
    SLOTSREMAINING_23 = 'SlotsRemaining 23'
    CHECK_BOX_3043 = 'Check Box 3043'
    SURVIVAL = 'Survival'
    SPELLS_1014 = 'Spells 1014'
    INTIMIDATION = 'Intimidation'
    SPELLS_1016 = 'Spells 1016'
    SPELLS_1017 = 'Spells 1017'
    CHECK_BOX_3037 = 'Check Box 3037'
    CHECK_BOX_3036 = 'Check Box 3036'
    CHECK_BOX_3035 = 'Check Box 3035'
    CHECK_BOX_3034 = 'Check Box 3034'
    CHECK_BOX_3033 = 'Check Box 3033'
    CHECK_BOX_3032 = 'Check Box 3032'
    BACKGROUND = 'Background'
    PROFBONUS = 'ProfBonus'
    CHARACTERNAME_2 = 'CharacterName 2'
    PROFICIENCIESLANG = 'ProficienciesLang'
    CHECK_BOX_3038 = 'Check Box 3038'
    SPELLS_1099 = 'Spells 1099'
    AC = 'AC'
    SPELLS_101013 = 'Spells 101013'
    SPELLS_1019 = 'Spells 1019'
    PLAYERNAME = 'PlayerName'
    SPELLS_10104 = 'Spells 10104'
    CHECK_BOX_3045 = 'Check Box 3045'
    SPELLS_1056 = 'Spells 1056'
    WPN1_DAMAGE = 'Wpn1 Damage'
    CHECK_BOX_326 = 'Check Box 326'
    SPELLS_1057 = 'Spells 1057'
    STR = 'STR'
    SLOTSREMAINING_19 = 'SlotsRemaining 19'
    ST_CHARISMA = 'ST Charisma'
    CHECK_BOX_3022 = 'Check Box 3022'
    CHECK_BOX_3083 = 'Check Box 3083'
    SPELLS_1083 = 'Spells 1083'
    SPELLS_1029 = 'Spells 1029'
    SPELLS_1028 = 'Spells 1028'
    CHECK_BOX_3039 = 'Check Box 3039'
    SPELLS_1025 = 'Spells 1025'
    SPELLS_1024 = 'Spells 1024'
    SPELLS_1027 = 'Spells 1027'
    SPELLS_1026 = 'Spells 1026'
    SPELLS_1021 = 'Spells 1021'
    SPELLS_1020 = 'Spells 1020'
    FEATURES_AND_TRAITS = 'Features and Traits'
    SPELLS_1022 = 'Spells 1022'
    CHECK_BOX_3042 = 'Check Box 3042'
    CHECK_BOX_3073 = 'Check Box 3073'
    CHECK_BOX_3040 = 'Check Box 3040'
    PERSONALITYTRAITS = 'PersonalityTraits '
    CHECK_BOX_3046 = 'Check Box 3046'
    CHECK_BOX_251 = 'Check Box 251'
    CHECK_BOX_3044 = 'Check Box 3044'
    CHECK_BOX_3072 = 'Check Box 3072'
    ATTACKSSPELLCASTING = 'AttacksSpellcasting'
    CHECK_BOX_3048 = 'Check Box 3048'
    CHECK_BOX_3049 = 'Check Box 3049'
    SPEED = 'Speed'
    CHECK_BOX_3071 = 'Check Box 3071'
    SLOTSREMAINING_21 = 'SlotsRemaining 21'



def split_xml_fields(text, splitType=u'\u22a0'):

    #return re.sub(r'[^\x00-\x7F]+',' ', text).split(' ')
    return re.split(splitType, text)

def get_ability_score_values(mainValue, saveProficency):

    abilityModifier = (int(mainValue)/2)-5
    saveThrow       = abilityModifier
    saveThrowProf   = False

    if saveProficency.lower() == 'true':
        saveThrow += 2
        saveThrowProf = True

    return str(abilityModifier), str(saveThrow), saveThrowProf

def get_skill_value(abilityModifier, profBonus, skillProf, doubleProf, halfProf, roundUp, miscBonus):

    skillValue = int(abilityModifier) + int(miscBonus)
    profBonus = int(profBonus)
    skillProfBool = False

    if skillProf.lower() == 'true':
        skillValue += profBonus
        skillProfBool = True
    if doubleProf.lower() == 'true':
        skillValue += profBonus
        skillProfBool = True
    if halfProf.lower() == 'ture':
        skillProfBool = True
        if roundUp.lower() == 'true':
            skillValue += int(math.ceil(float(profBonus)/2))
        else:
            skillValue += profBonus/2

    return str(skillValue), skillProfBool

def get_armor_class(armorBonus, miscArmorBonus, shieldBonus, maxDex):

    ac = int(armorBonus) + int(miscArmorBonus) + int(shieldBonus)

    return str(ac)

def get_attack_bonus(profBonus, profBool, abilityMod, magicBonus, miscBonus, weaponBonus):

    attackBonus = 0

    if profBool.lower() == 'true':
        attackBonus += profBonus

    attackBonus += abilityMod + magicBonus + miscBonus + weaponBonus

    return attackBonus

def get_damage_bonus(abilityMod, abilityModifierBool, magicBonus, miscBonus, weaponBonus):

    damageBonus = 0

    if abilityModifierBool.lower() == 'true':
        damageBonus += abilityMod

    damageBonus += magicBonus + miscBonus + weaponBonus

    #print 'damageBonus ', damageBonus
    return damageBonus

class Fifth_edition_app_parse:

    def __init__(self, outputClass):
        self.dict = dict(mainDict)

        self.oc = outputClass

        #print 'OUTPUT CLASS ', self.oc.CHARACTERNAME
        ##For debugging to show pdf field names
        ##for key in self.dict:
        ##    if self.dict[key] == '':
        ##        self.dict[key] = key

    def parse_hit_dice(self, root):

        hitDiceList = split_xml_fields(root.find('hitDiceList').text)

        self.dict[self.oc.HDTOTAL] = hitDiceList[1] + 'd' + hitDiceList[2]
        return

    def parse_ability_score(self, root):

        asList = split_xml_fields(root.find('abilityScores').text)

        self.dict[self.oc.STR] = asList[0]
        self.dict[self.oc.DEX] = asList[1]
        self.dict[self.oc.CON] = asList[2]
        self.dict[self.oc.INT] = asList[3]
        self.dict[self.oc.WIS] = asList[4]
        self.dict[self.oc.CHA] = asList[5]

        self.dict[self.oc.STRMOD], self.dict[self.oc.ST_STRENGTH], self.dict[self.oc.STR_PROF_CHECK_BOX] = get_ability_score_values(self.dict[self.oc.STR], asList[6])
        self.dict[self.oc.DEXMOD ], self.dict[self.oc.ST_DEXTERITY], self.dict[self.oc.DEX_PROF_CHECK_BOX] = get_ability_score_values(self.dict[self.oc.DEX], asList[7])
        self.dict[self.oc.CONMOD], self.dict[self.oc.ST_CONSTITUTION], self.dict[self.oc.CON_PROF_CHECK_BOX] = get_ability_score_values(self.dict[self.oc.CON], asList[8])
        self.dict[self.oc.INTMOD], self.dict[self.oc.ST_INTELLIGENCE], self.dict[self.oc.INT_PROF_CHECK_BOX] = get_ability_score_values(self.dict[self.oc.INT], asList[9])
        self.dict[self.oc.WISMOD], self.dict[self.oc.ST_WISDOM], self.dict[self.oc.WIS_PROF_CHECK_BOX] = get_ability_score_values(self.dict[self.oc.WIS], asList[10])
        self.dict[self.oc.CHAMOD], self.dict[self.oc.ST_CHARISMA], self.dict[self.oc.CHA_PROF_CHECK_BOX] = get_ability_score_values(self.dict[self.oc.CHA], asList[11])

        return

    def parse_skills(self, root):

        skill_list = split_xml_fields(root.find('skillInfo').text)

        #print len(skill_list)

        skillProf_list = skill_list[:19]
        miscBonus_list = skill_list[19:38]
        doubleProf_list = skill_list[38:57]
        halfProf_list = skill_list[57:76]
        roundUp_list = skill_list[76:95]

        #print len(skillProf_list), len(miscBonus_list), len(doubleProf_list), len(halfProf_list), len(roundUp_list)
        #print miscBonus_list[0], doubleProf_list[0], halfProf_list[0]
        #
        #print '1 ', skillProf_list
        #print '2 ', miscBonus_list
        #print '3 ', doubleProf_list
        #print '4 ' , halfProf_list
        #print '5 ' , roundUp_list

        pBonus = self.dict[self.oc.PROFBONUS]

        #Strength
        self.dict[self.oc.ATHLETICS], self.dict[self.oc.ATHLETICS_PROF] = get_skill_value(self.dict[self.oc.STRMOD], pBonus, skillProf_list[0], doubleProf_list[0], halfProf_list[0], roundUp_list[0],miscBonus_list[0])

        #Dexterity
        self.dict[self.oc.ACROBATICS], self.dict[self.oc.ACROBATICS_PROF] = get_skill_value(self.dict[self.oc.DEXMOD ], pBonus, skillProf_list[1], doubleProf_list[1], halfProf_list[1], roundUp_list[1], miscBonus_list[1])
        self.dict[self.oc.SLEIGHTOFHAND], self.dict[self.oc.SLEIGHTOFHAND_PROF] = get_skill_value(self.dict[self.oc.DEXMOD ], pBonus, skillProf_list[2],  doubleProf_list[2], halfProf_list[2], roundUp_list[2], miscBonus_list[2])
        self.dict[self.oc.STEALTH ], self.dict[self.oc.STEALTH_PROF] = get_skill_value(self.dict[self.oc.DEXMOD ], pBonus, skillProf_list[3],  doubleProf_list[3], halfProf_list[3], roundUp_list[3], miscBonus_list[3])

        #Intelligence
        self.dict[self.oc.ARCANA], self.dict[self.oc.ARCANA_PROF] = get_skill_value(self.dict[self.oc.INTMOD], pBonus, skillProf_list[4],  doubleProf_list[4], halfProf_list[4], roundUp_list[4], miscBonus_list[4])
        self.dict[self.oc.HISTORY ], self.dict[self.oc.HISTORY_PROF] = get_skill_value(self.dict[self.oc.INTMOD], pBonus, skillProf_list[5],  doubleProf_list[5], halfProf_list[5], roundUp_list[5], miscBonus_list[5])
        self.dict[self.oc.INVESTIGATION ], self.dict[self.oc.INVESTIGATION_PROF] = get_skill_value(self.dict[self.oc.INTMOD], pBonus, skillProf_list[6],  doubleProf_list[6], halfProf_list[6], roundUp_list[6], miscBonus_list[6])
        self.dict[self.oc.NATURE], self.dict[self.oc.NATURE_PROF] = get_skill_value(self.dict[self.oc.INTMOD], pBonus, skillProf_list[7],  doubleProf_list[7], halfProf_list[7], roundUp_list[7], miscBonus_list[7])
        self.dict[self.oc.RELIGION], self.dict[self.oc.RELIGION_PROF] = get_skill_value(self.dict[self.oc.INTMOD], pBonus, skillProf_list[8],  doubleProf_list[8], halfProf_list[8], roundUp_list[8], miscBonus_list[8])

        #Wisdom
        self.dict[self.oc.ANIMAL], self.dict[self.oc.ANIMAL_PROF] = get_skill_value(self.dict[self.oc.WISMOD], pBonus, skillProf_list[9],  doubleProf_list[9], halfProf_list[9], roundUp_list[9], miscBonus_list[9])
        self.dict[self.oc.INSIGHT], self.dict[self.oc.INSIGHT_PROF] = get_skill_value(self.dict[self.oc.WISMOD], pBonus, skillProf_list[10],  doubleProf_list[10], halfProf_list[10], roundUp_list[10], miscBonus_list[10])
        self.dict[self.oc.MEDICINE], self.dict[self.oc.MEDICINE_PROF] = get_skill_value(self.dict[self.oc.WISMOD], pBonus, skillProf_list[11],  doubleProf_list[11], halfProf_list[11], roundUp_list[11], miscBonus_list[11])
        self.dict[self.oc.PERCEPTION ], self.dict[self.oc.PERCEPTION_PROF] = get_skill_value(self.dict[self.oc.WISMOD], pBonus, skillProf_list[12],  doubleProf_list[12], halfProf_list[12], roundUp_list[12], miscBonus_list[12])
        self.dict[self.oc.SURVIVAL], self.dict[self.oc.SURVIVAL_PROF] = get_skill_value(self.dict[self.oc.WISMOD], pBonus, skillProf_list[13],  doubleProf_list[13], halfProf_list[13], roundUp_list[13], miscBonus_list[13])

        #Charisma
        self.dict[self.oc.DECEPTION ], self.dict[self.oc.DECEPTION_PROF] = get_skill_value(self.dict[self.oc.CHAMOD], pBonus, skillProf_list[14],  doubleProf_list[14], halfProf_list[14], roundUp_list[14], miscBonus_list[14])
        self.dict[self.oc.INTIMIDATION], self.dict[self.oc.INTIMIDATION_PROF] = get_skill_value(self.dict[self.oc.CHAMOD], pBonus, skillProf_list[15],  doubleProf_list[15], halfProf_list[15], roundUp_list[15], miscBonus_list[15])
        self.dict[self.oc.PERFORMANCE], self.dict[self.oc.PERFORMANCE_PROF] = get_skill_value(self.dict[self.oc.CHAMOD], pBonus, skillProf_list[16],  doubleProf_list[16], halfProf_list[16], roundUp_list[16], miscBonus_list[16])
        self.dict[self.oc.PERSUASION], self.dict[self.oc.PERSUASION_PROF] = get_skill_value(self.dict[self.oc.CHAMOD], pBonus, skillProf_list[17],  doubleProf_list[17], halfProf_list[17], roundUp_list[17], miscBonus_list[17])

        #Initiative
        self.dict[self.oc.INITIATIVE], _ = get_skill_value(self.dict[self.oc.DEXMOD ], pBonus, skillProf_list[18], doubleProf_list[18], halfProf_list[18], roundUp_list[18], root.find('initMiscMod').text)

        #Passive - use the same calc but give misc bonus of 10
        self.dict[self.oc.PASSIVE], _ = get_skill_value(self.dict[self.oc.WISMOD], pBonus, skillProf_list[12], '0', '0', '0', '10' )

        return

    def parse_armor_class(self, root):

        self.dict[self.oc.AC] = get_armor_class(root.find('armorBonus').text, \
                                        root.find('miscArmorBonus').text, \
                                        root.find('shieldBonus').text, \
                                        root.find('maxDex').text)

        return

    def parse_note_list(self, root):

        noteList = split_xml_fields(root.find('noteList').text)

        #i = 0
        #for item in noteList:
        #    print i, ' ', item.encode('utf-8')
        #    i+=1

        #Features
        self.dict[self.oc.FEATURES_AND_TRAITS] = noteList[0]

        #Languages and Profs
        armorProf = noteList[1]
        weaponProf = noteList[2]
        toolProf = noteList[3]
        languages = noteList[4]

        self.dict[self.oc.PROFICIENCIESLANG] = ' '.join(['Languages: ', re.sub('\n', ' . ', languages), \
                                                   '\nArmor Prof: ', re.sub('\n', ' . ', armorProf), \
                                                   '\nWeapon Prof:', re.sub('\n', ' . ', weaponProf), \
                                                   '\nTool Prof:', re.sub('\n', ' . ', toolProf)])

        #Equipment
        self.dict[self.oc.EQUIPMENT] = re.sub('\n', ' . ', noteList[5])

        #Also putting equipment into treasure incase of lack of room
        self.dict[self.oc.TREASURE] = re.sub('\n', ' . ', noteList[5])

        #Notes
        self.dict['Feat+Traits'] = noteList[6]

        #Class type
        #self.dict[self.oc.CLASSLEVEL] = noteList[7]

        #Race
        self.dict[self.oc.RACE ] = noteList[8]
        #Background
        self.dict[self.oc.BACKGROUND] = noteList[9]
        #Alignment
        self.dict[self.oc.ALIGNMENT] = noteList[10]

        #PersonalityTraits
        self.dict[self.oc.PERSONALITYTRAITS ] = noteList[11]
        #ideals
        self.dict[self.oc.IDEALS] = noteList[12]
        #Bonds
        self.dict[self.oc.BONDS] = noteList[13]
        #Flaws
        self.dict[self.oc.FLAWS] = noteList[14]

        #CharacterName
        self.dict[self.oc.CHARACTERNAME] = noteList[15]
        self.dict[self.oc.CHARACTERNAME_2] = noteList[15]

        #level (using this over class type)
        self.dict[self.oc.CLASSLEVEL] = noteList[16]

        #money
        self.dict[self.oc.CP] = noteList[17]
        self.dict[self.oc.SP] = noteList[18]
        self.dict[self.oc.EP] = noteList[19]
        self.dict[self.oc.GP] = noteList[20]
        self.dict[self.oc.PP] = noteList[21]

        #XP
        self.dict[self.oc.XP] = noteList[22]

        return

    def parse_death_saves(self, root):

        deathSaveSuccesses = root.find('deathSaveSuccesses').text
        deathSaveFailures  = root.find ('deathSaveFailures').text

        #Save - Set True if greater than value otherwise False
        self.dict[self.oc.DEATH_SAVE_SUCCESS_1] = int(deathSaveSuccesses) > 0
        self.dict[self.oc.DEATH_SAVE_SUCCESS_2] = int(deathSaveSuccesses) > 1
        self.dict[self.oc.DEATH_SAVE_SUCCESS_3] = int(deathSaveSuccesses) > 2

        #Failures
        self.dict[self.oc.DEATH_SAVE_FAIL_1] = int(deathSaveFailures) > 0
        self.dict[self.oc.DEATH_SAVE_FAIL_2] = int(deathSaveFailures) > 1
        self.dict[self.oc.DEATH_SAVE_FAIL_3] = int(deathSaveFailures) > 2


    def parse_bonus_list(self, list):

        #print list

        any_any = int(list[0])
        any_one = int(list[3])
        any_two = int(list[6])

        melee_any = int(list[1])
        melee_one = int(list[4])
        melee_two = int(list[7])

        ranged_any = int(list[2])
        ranged_one = int(list[5])
        ranged_two = int(list[8])

        return [any_any, any_one, any_two], [melee_any, melee_one, melee_two], [ranged_any, ranged_one, ranged_two]

    def parse_class_data(self, root):

        classDataList = split_xml_fields(root.find('classData').text, splitType=u'\u229f')

        classInfo = split_xml_fields(classDataList[0], splitType=u'\u22a1')
        #print classInfo
        archType = ""
        if classInfo[1] != "":
            archType = "{" + classInfo[1] + "}"
        self.classString = classInfo[0] + " " + archType

        #unknown
        attackBonusList = split_xml_fields(classDataList[10])
        damageBonusList = split_xml_fields(classDataList[11])

        self.weaponAttackAny,self.weaponAttackMelee,self.weaponAttackRanged = self.parse_bonus_list(attackBonusList)
        self.weaponDamageAny,self.weaponDamageMelee,self.weaponDamageRanged = self.parse_bonus_list(damageBonusList)


    def get_class_weapon_bonus(self, rangeType, numHands, any, melee, ranged):

        classBonus = any[0]

        #Melee
        if rangeType == '1':
            classBonus += melee[0]
            if numHands == '1':
                classBonus += any[1]
                classBonus += melee[1]
            if numHands == '2':
                classBonus += any[2]
                classBonus += melee[2]

        #Ranged
        if rangeType == '2':
            classBonus += ranged[0]
            if numHands == '1':
                classBonus += any[1]
                classBonus += ranged[1]
            if numHands == '2':
                classBonus += any[2]
                classBonus += ranged[2]

        #print 'classBonus ', classBonus
        return classBonus

    def parse_weapons(self, root):

        weaponList = split_xml_fields(root.find('weaponList').text)

        totalWeapons = weaponList[0]
        weapons = weaponList[1:]

        pBonus = int(self.dict[self.oc.PROFBONUS])
        attackAbilityList = [int(self.dict[self.oc.STRMOD]),
                             int(self.dict[self.oc.DEXMOD]),
                             int(self.dict[self.oc.CONMOD]),
                             int(self.dict[self.oc.INTMOD]),
                             int(self.dict[self.oc.WISMOD]),
                             int(self.dict[self.oc.CHAMOD])]

        weaponDamageTypeList = ['Bludgeon', 'Piercing', 'Slashing', 'Acid', 'Cold', 'Fire', 'Force',
                                'Lightning', 'Necrotic', 'Poison', 'Pysychic', 'Radiant', 'Thunder']

        #Split weapons into indidual lists
        #weapons = [weapons[i:i+13] for i in xrange(0, len(weapons), 13)]
        #print weapons
        #print 'Total weapon count: ', totalWeapons

        weaponOffset = 0
        restWeapons = ''
        for i in xrange(1, int(totalWeapons)+1):
            #print ('Weapon number {}'.format(i))

            #Get Info
            weaponInfo = weapons[weaponOffset:weaponOffset+10]
            weaponOffset +=10
            #print weaponInfo

            name = weaponInfo[0]
            range = weaponInfo[1]
            weaponCode = weaponInfo[2]

            attackAbilityCode = int(weaponInfo[3])
            magicAttackBonus = int(weaponInfo[4])
            miscAttackBonus = int(weaponInfo[5])
            magicDamageBonus = int(weaponInfo[6])
            miscDamageBonus = int(weaponInfo[7])
            weaponProfBool = weaponInfo[8]
            abilityModifierBool = weaponInfo[9]

            #get hitDice
            numHitDice = int(weapons[weaponOffset:weaponOffset+1][0])
            weaponOffset +=1

            #parse weaponCode
            if len(weaponCode) == 4:
                rangeType = weaponCode[0] #1 == melle, 2 == ranged
                numHands = weaponCode[1] #1 == one handed, 2 == two handed
                unknown = weaponCode[2]
                weaponDamageType = weaponDamageTypeList[int(weaponCode[3])]
            else:
                rangeType = 1
                numHands = 1
                weaponDamageType = weaponDamageTypeList[int(weaponCode[0])]

            #Get class weapon bonus
            classBonusDamage = self.get_class_weapon_bonus(rangeType, numHands, self.weaponDamageAny, self.weaponDamageMelee, self.weaponDamageRanged)
            classBonusAttack = self.get_class_weapon_bonus(rangeType, numHands, self.weaponAttackAny, self.weaponAttackMelee, self.weaponAttackRanged)

            #Parse hit dice
            hitDiceList = weapons[weaponOffset:weaponOffset+(numHitDice*2)]
            weaponOffset += (numHitDice*2)

            hitDice = ''
            for j in xrange(0, numHitDice):
                hitDice += hitDiceList[j*2] + 'd' + hitDiceList[j*2+1] + '+'

            #Get strings
            weaponAndRange = ' '.join([name, '(', range, ')'])
            weaponAttackBonus = get_attack_bonus(pBonus, \
                                                weaponProfBool, \
                                                attackAbilityList[attackAbilityCode], \
                                                magicAttackBonus, \
                                                miscAttackBonus, \
                                                0)
            weaponDamageBonus = get_damage_bonus(attackAbilityList[attackAbilityCode], \
                                                abilityModifierBool, \
                                                magicDamageBonus, \
                                                miscDamageBonus, \
                                                0)

            weaponAttackBonus = '+' + str(weaponAttackBonus + classBonusAttack)
            weaponDamageBonus = str(weaponDamageBonus + classBonusDamage)
            weaponDamage = hitDice + weaponDamageBonus + ' ' + weaponDamageType

            #print 'Weapon name: ', weaponAndRange
            #print 'Weapon attack: ', weaponAttackBonus
            #print 'weapon damage bonus: ', weaponDamageBonus
            #print 'Weapon damage: ', weaponDamage

            if i == 1:
                self.dict[self.oc.WPN_NAME] = weaponAndRange
                self.dict[self.oc.WPN1_ATKBONUS] = weaponAttackBonus
                self.dict[self.oc.WPN1_DAMAGE] = weaponDamage
            elif i == 2:
                self.dict[self.oc.WPN_NAME_2] = weaponAndRange
                self.dict[self.oc.WPN2_ATKBONUS ] = weaponAttackBonus
                self.dict[self.oc.WPN2_DAMAGE ] = weaponDamage
            elif i == 3:
                self.dict[self.oc.WPN_NAME_3] = weaponAndRange
                self.dict[self.oc.WPN3_ATKBONUS  ] = weaponAttackBonus
                self.dict[self.oc.WPN3_DAMAGE ] = weaponDamage
            else:
                restWeapons += ' '.join([weaponAndRange, ' [' + weaponAttackBonus + '] ', weaponDamage, '\n'])

        self.dict[self.oc.ATTACKSSPELLCASTING] = restWeapons
        return

    def parse_spells(self, root):

        spellList = split_xml_fields(root.find('spellList').text)

        spellListVerison = split_xml_fields(spellList[0], splitType=u'\u22a1')
        slotsRemaining = split_xml_fields(spellList[1], splitType=u'\u22a1')
        unknown2 = split_xml_fields(spellList[2], splitType=u'\u22a1')
        totalSpellSlots = split_xml_fields(spellList[3], splitType=u'\u22a1')
        unknown3 = split_xml_fields(spellList[4], splitType=u'\u22a1')
        unknown4 = split_xml_fields(spellList[5], splitType=u'\u22a1')
        spellLevel = split_xml_fields(spellList[6], splitType=u'\u22a1')
        unknown5 = split_xml_fields(spellList[7], splitType=u'\u22a1')
        spells = split_xml_fields(spellList[8], splitType=u'\u22a1')

        self.dict[self.oc.SPELLCASTING_CLASS_2] = "{} [Cast level {}]".format(self.classString,spellLevel[0])

        misc_dc_bonus = root.find('miscSpellDCBonus').text
        misc_attack_bonus = root.find('miscSpellAttackBonus').text

        #How do we know its int mod?
        abilityList = [int(self.dict[self.oc.STRMOD]),
                     int(self.dict[self.oc.DEXMOD]),
                     int(self.dict[self.oc.CONMOD]),
                     int(self.dict[self.oc.INTMOD]),
                     int(self.dict[self.oc.WISMOD]),
                     int(self.dict[self.oc.CHAMOD])]

        modifier_code = int(root.find('castingStatCode').text)
        modifier = abilityList[modifier_code]

        self.dict[self.oc.SPELLSAVEDC__2] = 8 + int(self.dict[self.oc.PROFBONUS]) + modifier + int(misc_dc_bonus)
        self.dict[self.oc.SPELLATKBONUS_2] = int(self.dict[self.oc.PROFBONUS]) + modifier + int(misc_attack_bonus)
        self.dict[self.oc.SPELLCASTINGABILITY_2] = modifier

        #Spell totals
        self.dict[self.oc.L1_SLOTSTOTAL] = totalSpellSlots[0]
        self.dict[self.oc.SLOTSTOTAL_20] = totalSpellSlots[1]
        self.dict[self.oc.SLOTSTOTAL_21] = totalSpellSlots[2]
        self.dict[self.oc.SLOTSTOTAL_22] = totalSpellSlots[3]
        self.dict[self.oc.SLOTSTOTAL_23] = totalSpellSlots[4]
        self.dict[self.oc.SLOTSTOTAL_24] = totalSpellSlots[5]
        self.dict[self.oc.SLOTSTOTAL_25] = totalSpellSlots[6]
        self.dict[self.oc.SLOTSTOTAL_26] = totalSpellSlots[7]
        self.dict[self.oc.SLOTSTOTAL_27] = totalSpellSlots[8]

        #Slots Remaining
        #print 'Slots remaining', slotsRemaining
        self.dict[self.oc.SLOTSREMAINING_19] = "{}/{} remaining".format(slotsRemaining[0],totalSpellSlots[0])
        self.dict[self.oc.SLOTSREMAINING_20] = "{}/{} remaining".format(slotsRemaining[1],totalSpellSlots[1])
        self.dict[self.oc.SLOTSREMAINING_21] = "{}/{} remaining".format(slotsRemaining[2],totalSpellSlots[2])
        self.dict[self.oc.SLOTSREMAINING_22] = "{}/{} remaining".format(slotsRemaining[3],totalSpellSlots[3])
        self.dict[self.oc.SLOTSREMAINING_23] = "{}/{} remaining".format(slotsRemaining[4],totalSpellSlots[4])
        self.dict[self.oc.SLOTSREMAINING_24] = "{}/{} remaining".format(slotsRemaining[5],totalSpellSlots[5])
        self.dict[self.oc.SLOTSREMAINING_25] = "{}/{} remaining".format(slotsRemaining[6],totalSpellSlots[6])
        self.dict[self.oc.SLOTSREMAINING_26] = "{}/{} remaining".format(slotsRemaining[7],totalSpellSlots[7])
        self.dict[self.oc.SLOTSREMAINING_27] = "{}/{} remaining".format(slotsRemaining[8],totalSpellSlots[8])

        CANTRIP_SLOTS = [(self.oc.SPELLS_1014,"checkbox"),
                        (self.oc.SPELLS_1016, "check"),
                        (self.oc.SPELLS_1017, "check"),
                        (self.oc.SPELLS_1018, "check"),
                        (self.oc.SPELLS_1019, "check"),
                        (self.oc.SPELLS_1020, "check"),
                        (self.oc.SPELLS_1021, "check"),
                        (self.oc.SPELLS_1022, "check")]
        LEVEL_1 = [(self.oc.SPELLS_1015, self.oc.CHECK_BOX_251),
                   (self.oc.SPELLS_1023, self.oc.CHECK_BOX_309),
                   (self.oc.SPELLS_1024, self.oc.CHECK_BOX_3010),
                   (self.oc.SPELLS_1025, self.oc.CHECK_BOX_3011),
                   (self.oc.SPELLS_1026, self.oc.CHECK_BOX_3012),
                   (self.oc.SPELLS_1027, self.oc.CHECK_BOX_3013),
                   (self.oc.SPELLS_1028, self.oc.CHECK_BOX_3014),
                   (self.oc.SPELLS_1029, self.oc.CHECK_BOX_3015),
                   (self.oc.SPELLS_1030, self.oc.CHECK_BOX_3016),
                   (self.oc.SPELLS_1031, self.oc.CHECK_BOX_3017),
                   (self.oc.SPELLS_1032, self.oc.CHECK_BOX_3018),
                   (self.oc.SPELLS_1033, self.oc.CHECK_BOX_3019),
                    ]
        LEVEL_2 = [(self.oc.SPELLS_1046, self.oc.CHECK_BOX_313),
                   (self.oc.SPELLS_1034, self.oc.CHECK_BOX_310),
                   (self.oc.SPELLS_1035, self.oc.CHECK_BOX_3020),
                   (self.oc.SPELLS_1036, self.oc.CHECK_BOX_3021),
                   (self.oc.SPELLS_1037, self.oc.CHECK_BOX_3022),
                   (self.oc.SPELLS_1038, self.oc.CHECK_BOX_3023),
                   (self.oc.SPELLS_1039, self.oc.CHECK_BOX_3024),
                   (self.oc.SPELLS_1040, self.oc.CHECK_BOX_3025),
                   (self.oc.SPELLS_1041, self.oc.CHECK_BOX_3026),
                   (self.oc.SPELLS_1042, self.oc.CHECK_BOX_3027),
                   (self.oc.SPELLS_1043, self.oc.CHECK_BOX_3028),
                   (self.oc.SPELLS_1044, self.oc.CHECK_BOX_3029),
                   (self.oc.SPELLS_1045, self.oc.CHECK_BOX_3030),
                    ]

        LEVEL_3 = [(self.oc.SPELLS_1048, self.oc.CHECK_BOX_315),
                   (self.oc.SPELLS_1047, self.oc.CHECK_BOX_314),
                   (self.oc.SPELLS_1049, self.oc.CHECK_BOX_3031),
                   (self.oc.SPELLS_1050, self.oc.CHECK_BOX_3032),
                   (self.oc.SPELLS_1051, self.oc.CHECK_BOX_3033),
                   (self.oc.SPELLS_1052, self.oc.CHECK_BOX_3034),
                   (self.oc.SPELLS_1053, self.oc.CHECK_BOX_3035),
                   (self.oc.SPELLS_1054, self.oc.CHECK_BOX_3036),
                   (self.oc.SPELLS_1055, self.oc.CHECK_BOX_3037),
                   (self.oc.SPELLS_1056, self.oc.CHECK_BOX_3038),
                   (self.oc.SPELLS_1057, self.oc.CHECK_BOX_3039),
                   (self.oc.SPELLS_1058, self.oc.CHECK_BOX_3040),
                   (self.oc.SPELLS_1059, self.oc.CHECK_BOX_3041),
                    ]

        LEVEL_4 = [(self.oc.SPELLS_1061, self.oc.CHECK_BOX_317),
                   (self.oc.SPELLS_1060, self.oc.CHECK_BOX_316),
                   (self.oc.SPELLS_1062, self.oc.CHECK_BOX_3042),
                   (self.oc.SPELLS_1063, self.oc.CHECK_BOX_3043),
                   (self.oc.SPELLS_1064, self.oc.CHECK_BOX_3044),
                   (self.oc.SPELLS_1065, self.oc.CHECK_BOX_3045),
                   (self.oc.SPELLS_1066, self.oc.CHECK_BOX_3046),
                   (self.oc.SPELLS_1067, self.oc.CHECK_BOX_3047),
                   (self.oc.SPELLS_1068, self.oc.CHECK_BOX_3048),
                   (self.oc.SPELLS_1069, self.oc.CHECK_BOX_3049),
                   (self.oc.SPELLS_1070, self.oc.CHECK_BOX_3050),
                   (self.oc.SPELLS_1071, self.oc.CHECK_BOX_3051),
                   (self.oc.SPELLS_1072, self.oc.CHECK_BOX_3052),
                    ]

        LEVEL_5 = [(self.oc.SPELLS_1074, self.oc.CHECK_BOX_319),
                   (self.oc.SPELLS_1073, self.oc.CHECK_BOX_318),
                   (self.oc.SPELLS_1075, self.oc.CHECK_BOX_3053),
                   (self.oc.SPELLS_1076, self.oc.CHECK_BOX_3054),
                   (self.oc.SPELLS_1077, self.oc.CHECK_BOX_3055),
                   (self.oc.SPELLS_1078, self.oc.CHECK_BOX_3056),
                   (self.oc.SPELLS_1079, self.oc.CHECK_BOX_3057),
                   (self.oc.SPELLS_1080, self.oc.CHECK_BOX_3058),
                   (self.oc.SPELLS_1081, self.oc.CHECK_BOX_3059),
                    ]
        LEVEL_6 = [(self.oc.SPELLS_1083, self.oc.CHECK_BOX_321),
                   (self.oc.SPELLS_1082, self.oc.CHECK_BOX_320),
                   (self.oc.SPELLS_1084, self.oc.CHECK_BOX_3060),
                   (self.oc.SPELLS_1085, self.oc.CHECK_BOX_3061),
                   (self.oc.SPELLS_1086, self.oc.CHECK_BOX_3062),
                   (self.oc.SPELLS_1087, self.oc.CHECK_BOX_3063),
                   (self.oc.SPELLS_1088, self.oc.CHECK_BOX_3064),
                   (self.oc.SPELLS_1089, self.oc.CHECK_BOX_3065),
                   (self.oc.SPELLS_1090, self.oc.CHECK_BOX_3066),
                    ]
        LEVEL_7 = [(self.oc.SPELLS_1092, self.oc.CHECK_BOX_323),
                   (self.oc.SPELLS_1091, self.oc.CHECK_BOX_322),
                   (self.oc.SPELLS_1093, self.oc.CHECK_BOX_3067),
                   (self.oc.SPELLS_1094, self.oc.CHECK_BOX_3068),
                   (self.oc.SPELLS_1095, self.oc.CHECK_BOX_3069),
                   (self.oc.SPELLS_1096, self.oc.CHECK_BOX_3070),
                   (self.oc.SPELLS_1097, self.oc.CHECK_BOX_3071),
                   (self.oc.SPELLS_1098, self.oc.CHECK_BOX_3072),
                   (self.oc.SPELLS_1099, self.oc.CHECK_BOX_3073),
                    ]
        LEVEL_8 = [(self.oc.SPELLS_10101, self.oc.CHECK_BOX_325),
                   (self.oc.SPELLS_10100, self.oc.CHECK_BOX_324),
                   (self.oc.SPELLS_10102, self.oc.CHECK_BOX_3074),
                   (self.oc.SPELLS_10103, self.oc.CHECK_BOX_3075),
                   (self.oc.SPELLS_10104, self.oc.CHECK_BOX_3076),
                   (self.oc.SPELLS_10105, self.oc.CHECK_BOX_3077),
                   (self.oc.SPELLS_10106, self.oc.CHECK_BOX_3078),
                    ]
        LEVEL_9 = [(self.oc.SPELLS_10108, self.oc.CHECK_BOX_327),
                   (self.oc.SPELLS_10107, self.oc.CHECK_BOX_326),
                   (self.oc.SPELLS_10109, self.oc.CHECK_BOX_3079),
                   (self.oc.SPELLS_101010, self.oc.CHECK_BOX_3080),
                   (self.oc.SPELLS_101011, self.oc.CHECK_BOX_3081),
                   (self.oc.SPELLS_101012, self.oc.CHECK_BOX_3082),
                   (self.oc.SPELLS_101013, self.oc.CHECK_BOX_3083),
                    ]

        spell_slots = [CANTRIP_SLOTS, LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5,
                       LEVEL_6, LEVEL_7, LEVEL_8, LEVEL_9]

        #print spells
        for spell in spells[:-1]:
            spell_list = split_xml_fields(spell, splitType=u'\u229f')
            level = int(spell_list[0])
            name = spell_list[1]
            prepared = spell_list[7]

            try:
                slot,prep = spell_slots[level].pop(0)
            except:
                continue

            self.dict[slot] = name
            if "true" == prepared:
                self.dict[prep] = True


        return

    def parse_5e_app_xml_character(self, fileName):

        print('Converting {} into {}'.format(fileName, self.oc.output_name))
        tree = ET.parse(fileName)
        root = tree.getroot()

        self.dict[self.oc.PROFBONUS] = root.find('proficiencyBonus').text
        self.dict[self.oc.HPMAX] = root.find('maxHealth').text
        self.dict[self.oc.HPCURRENT] = root.find('currentHealth').text
        self.dict[self.oc.HPTEMP] = root.find('currentTempHP').text
        self.dict[self.oc.SPEED] = str(int(root.find('baseSpeed').text) + int(root.find('speedMiscMod').text))

        #Lazy error handling if the xml dosn't contain one of the fields then just
        #continue and try and do the rest, put into blocks of 2 to save space
        functions_to_call = [
                        self.parse_class_data,
                        self.parse_armor_class,
                        self.parse_hit_dice,
                        self.parse_ability_score,
                        self.parse_skills,
                        self.parse_note_list,
                        self.parse_death_saves,
                        self.parse_weapons,
                        self.parse_spells
                            ]

        for function in functions_to_call:
            try:
                function(root)
            except Exception as e:
                print("\nERROR: Failed to run {} so not outputting. The error is \n\n{}\n\n".format(function.__name__, e))
                traceback.print_exc(file=sys.stdout)



        return self.dict


def output(dict, input_pdf, fdf_name, output_name):

    fields = dict.items()

    fdf = forge_fdf("", fields, [], [], [])
    fdf_file = open(fdf_name, 'wb')
    fdf_file.write(fdf)
    fdf_file.close()

    cmd = 'pdftk "{0}" fill_form "{1}" output "{2}" dont_ask'.format(
            input_pdf, #input pdf
            fdf_name, #input fdf
            os.path.join('output', output_name) #output
        )
    #print('About to send this command to pdftk: ' + cmd)
    os.system(cmd)

    return

def main():

    output_classes = [CharacterSheet, AlternativeCharacterSheet]

    if not os.path.exists("input"):
        print("Can't find input folder. Please put character file into a folder called 'input'")
        time.sleep(10)
        sys.exit(1)

    if not os.path.exists('output'):
        os.mkdir('output')

    for xmlfile in os.listdir("input"):
        for output_class in output_classes:

            app_xml_parser = Fifth_edition_app_parse(output_class)
            dict = app_xml_parser.parse_5e_app_xml_character(os.path.join('input', xmlfile))

            #input_pdf = 'DnD_5E_CharacterSheet - Form Fillable.pdf'
            #input_pdf = 'Character Sheet - Alternative - Form Fillable.pdf'
            input_pdf = app_xml_parser.oc.input_pdf
            fdf_name = 'Character Sheet - Form Filable.fdf'
            output_name = xmlfile + "_" + output_class.output_name + '.pdf'

            output(dict, input_pdf, fdf_name, output_name)



if __name__ == "__main__":
    print("Hello. Lets make some pdfs!!")
    try:
        main()
        print("FINISHED!!")
    except Exception as e:
        print("Failed to run :( error is here [{}]".format(e))

    time.sleep(10)
    sys.exit(0)

