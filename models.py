# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DatasBase(models.Model):
    datas_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField(blank=True, null=True)
    index_pnt_in_file = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()
    time_in_mjd = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    type_of_data = models.IntegerField(blank=True, null=True)
    usability = models.FloatField(blank=True, null=True)
    nbands = models.IntegerField()
    cnl_001 = models.FloatField(blank=True, null=True)
    cnl_002 = models.FloatField(blank=True, null=True)
    cnl_003 = models.FloatField(blank=True, null=True)
    cnl_004 = models.FloatField(blank=True, null=True)
    cnl_005 = models.FloatField(blank=True, null=True)
    cnl_006 = models.FloatField(blank=True, null=True)
    cnl_007 = models.FloatField(blank=True, null=True)
    cnl_008 = models.FloatField(blank=True, null=True)
    cnl_009 = models.FloatField(blank=True, null=True)
    cnl_010 = models.FloatField(blank=True, null=True)
    cnl_011 = models.FloatField(blank=True, null=True)
    cnl_012 = models.FloatField(blank=True, null=True)
    cnl_013 = models.FloatField(blank=True, null=True)
    cnl_014 = models.FloatField(blank=True, null=True)
    cnl_015 = models.FloatField(blank=True, null=True)
    cnl_016 = models.FloatField(blank=True, null=True)
    cnl_017 = models.FloatField(blank=True, null=True)
    cnl_018 = models.FloatField(blank=True, null=True)
    cnl_019 = models.FloatField(blank=True, null=True)
    cnl_020 = models.FloatField(blank=True, null=True)
    cnl_021 = models.FloatField(blank=True, null=True)
    cnl_022 = models.FloatField(blank=True, null=True)
    cnl_023 = models.FloatField(blank=True, null=True)
    cnl_024 = models.FloatField(blank=True, null=True)
    cnl_025 = models.FloatField(blank=True, null=True)
    cnl_026 = models.FloatField(blank=True, null=True)
    cnl_027 = models.FloatField(blank=True, null=True)
    cnl_028 = models.FloatField(blank=True, null=True)
    cnl_029 = models.FloatField(blank=True, null=True)
    cnl_030 = models.FloatField(blank=True, null=True)
    cnl_031 = models.FloatField(blank=True, null=True)
    cnl_032 = models.FloatField(blank=True, null=True)
    cnl_033 = models.FloatField(blank=True, null=True)
    cnl_034 = models.FloatField(blank=True, null=True)
    cnl_035 = models.FloatField(blank=True, null=True)
    cnl_036 = models.FloatField(blank=True, null=True)
    cnl_037 = models.FloatField(blank=True, null=True)
    cnl_038 = models.FloatField(blank=True, null=True)
    cnl_039 = models.FloatField(blank=True, null=True)
    cnl_040 = models.FloatField(blank=True, null=True)
    cnl_041 = models.FloatField(blank=True, null=True)
    cnl_042 = models.FloatField(blank=True, null=True)
    cnl_043 = models.FloatField(blank=True, null=True)
    cnl_044 = models.FloatField(blank=True, null=True)
    cnl_045 = models.FloatField(blank=True, null=True)
    cnl_046 = models.FloatField(blank=True, null=True)
    cnl_047 = models.FloatField(blank=True, null=True)
    cnl_048 = models.FloatField(blank=True, null=True)
    cnl_049 = models.FloatField(blank=True, null=True)
    cnl_050 = models.FloatField(blank=True, null=True)
    cnl_051 = models.FloatField(blank=True, null=True)
    cnl_052 = models.FloatField(blank=True, null=True)
    cnl_053 = models.FloatField(blank=True, null=True)
    cnl_054 = models.FloatField(blank=True, null=True)
    cnl_055 = models.FloatField(blank=True, null=True)
    cnl_056 = models.FloatField(blank=True, null=True)
    cnl_057 = models.FloatField(blank=True, null=True)
    cnl_058 = models.FloatField(blank=True, null=True)
    cnl_059 = models.FloatField(blank=True, null=True)
    cnl_060 = models.FloatField(blank=True, null=True)
    cnl_061 = models.FloatField(blank=True, null=True)
    cnl_062 = models.FloatField(blank=True, null=True)
    cnl_063 = models.FloatField(blank=True, null=True)
    cnl_064 = models.FloatField(blank=True, null=True)
    cnl_065 = models.FloatField(blank=True, null=True)
    cnl_066 = models.FloatField(blank=True, null=True)
    cnl_067 = models.FloatField(blank=True, null=True)
    cnl_068 = models.FloatField(blank=True, null=True)
    cnl_069 = models.FloatField(blank=True, null=True)
    cnl_070 = models.FloatField(blank=True, null=True)
    cnl_071 = models.FloatField(blank=True, null=True)
    cnl_072 = models.FloatField(blank=True, null=True)
    cnl_073 = models.FloatField(blank=True, null=True)
    cnl_074 = models.FloatField(blank=True, null=True)
    cnl_075 = models.FloatField(blank=True, null=True)
    cnl_076 = models.FloatField(blank=True, null=True)
    cnl_077 = models.FloatField(blank=True, null=True)
    cnl_078 = models.FloatField(blank=True, null=True)
    cnl_079 = models.FloatField(blank=True, null=True)
    cnl_080 = models.FloatField(blank=True, null=True)
    cnl_081 = models.FloatField(blank=True, null=True)
    cnl_082 = models.FloatField(blank=True, null=True)
    cnl_083 = models.FloatField(blank=True, null=True)
    cnl_084 = models.FloatField(blank=True, null=True)
    cnl_085 = models.FloatField(blank=True, null=True)
    cnl_086 = models.FloatField(blank=True, null=True)
    cnl_087 = models.FloatField(blank=True, null=True)
    cnl_088 = models.FloatField(blank=True, null=True)
    cnl_089 = models.FloatField(blank=True, null=True)
    cnl_090 = models.FloatField(blank=True, null=True)
    cnl_091 = models.FloatField(blank=True, null=True)
    cnl_092 = models.FloatField(blank=True, null=True)
    cnl_093 = models.FloatField(blank=True, null=True)
    cnl_094 = models.FloatField(blank=True, null=True)
    cnl_095 = models.FloatField(blank=True, null=True)
    cnl_096 = models.FloatField(blank=True, null=True)
    cnl_097 = models.FloatField(blank=True, null=True)
    cnl_098 = models.FloatField(blank=True, null=True)
    cnl_099 = models.FloatField(blank=True, null=True)
    cnl_100 = models.FloatField(blank=True, null=True)
    cnl_101 = models.FloatField(blank=True, null=True)
    cnl_102 = models.FloatField(blank=True, null=True)
    cnl_103 = models.FloatField(blank=True, null=True)
    cnl_104 = models.FloatField(blank=True, null=True)
    cnl_105 = models.FloatField(blank=True, null=True)
    cnl_106 = models.FloatField(blank=True, null=True)
    cnl_107 = models.FloatField(blank=True, null=True)
    cnl_108 = models.FloatField(blank=True, null=True)
    cnl_109 = models.FloatField(blank=True, null=True)
    cnl_110 = models.FloatField(blank=True, null=True)
    cnl_111 = models.FloatField(blank=True, null=True)
    cnl_112 = models.FloatField(blank=True, null=True)
    cnl_113 = models.FloatField(blank=True, null=True)
    cnl_114 = models.FloatField(blank=True, null=True)
    cnl_115 = models.FloatField(blank=True, null=True)
    cnl_116 = models.FloatField(blank=True, null=True)
    cnl_117 = models.FloatField(blank=True, null=True)
    cnl_118 = models.FloatField(blank=True, null=True)
    cnl_119 = models.FloatField(blank=True, null=True)
    cnl_120 = models.FloatField(blank=True, null=True)
    cnl_121 = models.FloatField(blank=True, null=True)
    cnl_122 = models.FloatField(blank=True, null=True)
    cnl_123 = models.FloatField(blank=True, null=True)
    cnl_124 = models.FloatField(blank=True, null=True)
    cnl_125 = models.FloatField(blank=True, null=True)
    cnl_126 = models.FloatField(blank=True, null=True)
    cnl_127 = models.FloatField(blank=True, null=True)
    cnl_128 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datas_base'


class DatasBaseCalb(models.Model):
    datas_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField(blank=True, null=True)
    index_pnt_in_file = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()
    time_in_mjd = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    type_of_data = models.IntegerField(blank=True, null=True)
    usability = models.FloatField(blank=True, null=True)
    nbands = models.IntegerField()
    type_of_calb = models.IntegerField(blank=True, null=True)
    index_in_mv = models.IntegerField(blank=True, null=True)
    cnl_001 = models.FloatField(blank=True, null=True)
    cnl_002 = models.FloatField(blank=True, null=True)
    cnl_003 = models.FloatField(blank=True, null=True)
    cnl_004 = models.FloatField(blank=True, null=True)
    cnl_005 = models.FloatField(blank=True, null=True)
    cnl_006 = models.FloatField(blank=True, null=True)
    cnl_007 = models.FloatField(blank=True, null=True)
    cnl_008 = models.FloatField(blank=True, null=True)
    cnl_009 = models.FloatField(blank=True, null=True)
    cnl_010 = models.FloatField(blank=True, null=True)
    cnl_011 = models.FloatField(blank=True, null=True)
    cnl_012 = models.FloatField(blank=True, null=True)
    cnl_013 = models.FloatField(blank=True, null=True)
    cnl_014 = models.FloatField(blank=True, null=True)
    cnl_015 = models.FloatField(blank=True, null=True)
    cnl_016 = models.FloatField(blank=True, null=True)
    cnl_017 = models.FloatField(blank=True, null=True)
    cnl_018 = models.FloatField(blank=True, null=True)
    cnl_019 = models.FloatField(blank=True, null=True)
    cnl_020 = models.FloatField(blank=True, null=True)
    cnl_021 = models.FloatField(blank=True, null=True)
    cnl_022 = models.FloatField(blank=True, null=True)
    cnl_023 = models.FloatField(blank=True, null=True)
    cnl_024 = models.FloatField(blank=True, null=True)
    cnl_025 = models.FloatField(blank=True, null=True)
    cnl_026 = models.FloatField(blank=True, null=True)
    cnl_027 = models.FloatField(blank=True, null=True)
    cnl_028 = models.FloatField(blank=True, null=True)
    cnl_029 = models.FloatField(blank=True, null=True)
    cnl_030 = models.FloatField(blank=True, null=True)
    cnl_031 = models.FloatField(blank=True, null=True)
    cnl_032 = models.FloatField(blank=True, null=True)
    cnl_033 = models.FloatField(blank=True, null=True)
    cnl_034 = models.FloatField(blank=True, null=True)
    cnl_035 = models.FloatField(blank=True, null=True)
    cnl_036 = models.FloatField(blank=True, null=True)
    cnl_037 = models.FloatField(blank=True, null=True)
    cnl_038 = models.FloatField(blank=True, null=True)
    cnl_039 = models.FloatField(blank=True, null=True)
    cnl_040 = models.FloatField(blank=True, null=True)
    cnl_041 = models.FloatField(blank=True, null=True)
    cnl_042 = models.FloatField(blank=True, null=True)
    cnl_043 = models.FloatField(blank=True, null=True)
    cnl_044 = models.FloatField(blank=True, null=True)
    cnl_045 = models.FloatField(blank=True, null=True)
    cnl_046 = models.FloatField(blank=True, null=True)
    cnl_047 = models.FloatField(blank=True, null=True)
    cnl_048 = models.FloatField(blank=True, null=True)
    cnl_049 = models.FloatField(blank=True, null=True)
    cnl_050 = models.FloatField(blank=True, null=True)
    cnl_051 = models.FloatField(blank=True, null=True)
    cnl_052 = models.FloatField(blank=True, null=True)
    cnl_053 = models.FloatField(blank=True, null=True)
    cnl_054 = models.FloatField(blank=True, null=True)
    cnl_055 = models.FloatField(blank=True, null=True)
    cnl_056 = models.FloatField(blank=True, null=True)
    cnl_057 = models.FloatField(blank=True, null=True)
    cnl_058 = models.FloatField(blank=True, null=True)
    cnl_059 = models.FloatField(blank=True, null=True)
    cnl_060 = models.FloatField(blank=True, null=True)
    cnl_061 = models.FloatField(blank=True, null=True)
    cnl_062 = models.FloatField(blank=True, null=True)
    cnl_063 = models.FloatField(blank=True, null=True)
    cnl_064 = models.FloatField(blank=True, null=True)
    cnl_065 = models.FloatField(blank=True, null=True)
    cnl_066 = models.FloatField(blank=True, null=True)
    cnl_067 = models.FloatField(blank=True, null=True)
    cnl_068 = models.FloatField(blank=True, null=True)
    cnl_069 = models.FloatField(blank=True, null=True)
    cnl_070 = models.FloatField(blank=True, null=True)
    cnl_071 = models.FloatField(blank=True, null=True)
    cnl_072 = models.FloatField(blank=True, null=True)
    cnl_073 = models.FloatField(blank=True, null=True)
    cnl_074 = models.FloatField(blank=True, null=True)
    cnl_075 = models.FloatField(blank=True, null=True)
    cnl_076 = models.FloatField(blank=True, null=True)
    cnl_077 = models.FloatField(blank=True, null=True)
    cnl_078 = models.FloatField(blank=True, null=True)
    cnl_079 = models.FloatField(blank=True, null=True)
    cnl_080 = models.FloatField(blank=True, null=True)
    cnl_081 = models.FloatField(blank=True, null=True)
    cnl_082 = models.FloatField(blank=True, null=True)
    cnl_083 = models.FloatField(blank=True, null=True)
    cnl_084 = models.FloatField(blank=True, null=True)
    cnl_085 = models.FloatField(blank=True, null=True)
    cnl_086 = models.FloatField(blank=True, null=True)
    cnl_087 = models.FloatField(blank=True, null=True)
    cnl_088 = models.FloatField(blank=True, null=True)
    cnl_089 = models.FloatField(blank=True, null=True)
    cnl_090 = models.FloatField(blank=True, null=True)
    cnl_091 = models.FloatField(blank=True, null=True)
    cnl_092 = models.FloatField(blank=True, null=True)
    cnl_093 = models.FloatField(blank=True, null=True)
    cnl_094 = models.FloatField(blank=True, null=True)
    cnl_095 = models.FloatField(blank=True, null=True)
    cnl_096 = models.FloatField(blank=True, null=True)
    cnl_097 = models.FloatField(blank=True, null=True)
    cnl_098 = models.FloatField(blank=True, null=True)
    cnl_099 = models.FloatField(blank=True, null=True)
    cnl_100 = models.FloatField(blank=True, null=True)
    cnl_101 = models.FloatField(blank=True, null=True)
    cnl_102 = models.FloatField(blank=True, null=True)
    cnl_103 = models.FloatField(blank=True, null=True)
    cnl_104 = models.FloatField(blank=True, null=True)
    cnl_105 = models.FloatField(blank=True, null=True)
    cnl_106 = models.FloatField(blank=True, null=True)
    cnl_107 = models.FloatField(blank=True, null=True)
    cnl_108 = models.FloatField(blank=True, null=True)
    cnl_109 = models.FloatField(blank=True, null=True)
    cnl_110 = models.FloatField(blank=True, null=True)
    cnl_111 = models.FloatField(blank=True, null=True)
    cnl_112 = models.FloatField(blank=True, null=True)
    cnl_113 = models.FloatField(blank=True, null=True)
    cnl_114 = models.FloatField(blank=True, null=True)
    cnl_115 = models.FloatField(blank=True, null=True)
    cnl_116 = models.FloatField(blank=True, null=True)
    cnl_117 = models.FloatField(blank=True, null=True)
    cnl_118 = models.FloatField(blank=True, null=True)
    cnl_119 = models.FloatField(blank=True, null=True)
    cnl_120 = models.FloatField(blank=True, null=True)
    cnl_121 = models.FloatField(blank=True, null=True)
    cnl_122 = models.FloatField(blank=True, null=True)
    cnl_123 = models.FloatField(blank=True, null=True)
    cnl_124 = models.FloatField(blank=True, null=True)
    cnl_125 = models.FloatField(blank=True, null=True)
    cnl_126 = models.FloatField(blank=True, null=True)
    cnl_127 = models.FloatField(blank=True, null=True)
    cnl_128 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datas_base_calb'


class DatasBaseCalbOfMidRange(models.Model):
    datas_id = models.AutoField(primary_key=True)
    time_start = models.DateTimeField()
    time_stop = models.DateTimeField()
    time_in_mjd_start = models.FloatField(blank=True, null=True)
    time_in_mjd_stop = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    n_point_in_range = models.IntegerField(blank=True, null=True)
    type_of_averaging = models.IntegerField(blank=True, null=True)
    type_of_data = models.IntegerField(blank=True, null=True)
    nbands = models.IntegerField()
    type_of_calb = models.IntegerField(blank=True, null=True)
    index_in_mv = models.IntegerField(blank=True, null=True)
    cnl_001 = models.FloatField(blank=True, null=True)
    cnl_002 = models.FloatField(blank=True, null=True)
    cnl_003 = models.FloatField(blank=True, null=True)
    cnl_004 = models.FloatField(blank=True, null=True)
    cnl_005 = models.FloatField(blank=True, null=True)
    cnl_006 = models.FloatField(blank=True, null=True)
    cnl_007 = models.FloatField(blank=True, null=True)
    cnl_008 = models.FloatField(blank=True, null=True)
    cnl_009 = models.FloatField(blank=True, null=True)
    cnl_010 = models.FloatField(blank=True, null=True)
    cnl_011 = models.FloatField(blank=True, null=True)
    cnl_012 = models.FloatField(blank=True, null=True)
    cnl_013 = models.FloatField(blank=True, null=True)
    cnl_014 = models.FloatField(blank=True, null=True)
    cnl_015 = models.FloatField(blank=True, null=True)
    cnl_016 = models.FloatField(blank=True, null=True)
    cnl_017 = models.FloatField(blank=True, null=True)
    cnl_018 = models.FloatField(blank=True, null=True)
    cnl_019 = models.FloatField(blank=True, null=True)
    cnl_020 = models.FloatField(blank=True, null=True)
    cnl_021 = models.FloatField(blank=True, null=True)
    cnl_022 = models.FloatField(blank=True, null=True)
    cnl_023 = models.FloatField(blank=True, null=True)
    cnl_024 = models.FloatField(blank=True, null=True)
    cnl_025 = models.FloatField(blank=True, null=True)
    cnl_026 = models.FloatField(blank=True, null=True)
    cnl_027 = models.FloatField(blank=True, null=True)
    cnl_028 = models.FloatField(blank=True, null=True)
    cnl_029 = models.FloatField(blank=True, null=True)
    cnl_030 = models.FloatField(blank=True, null=True)
    cnl_031 = models.FloatField(blank=True, null=True)
    cnl_032 = models.FloatField(blank=True, null=True)
    cnl_033 = models.FloatField(blank=True, null=True)
    cnl_034 = models.FloatField(blank=True, null=True)
    cnl_035 = models.FloatField(blank=True, null=True)
    cnl_036 = models.FloatField(blank=True, null=True)
    cnl_037 = models.FloatField(blank=True, null=True)
    cnl_038 = models.FloatField(blank=True, null=True)
    cnl_039 = models.FloatField(blank=True, null=True)
    cnl_040 = models.FloatField(blank=True, null=True)
    cnl_041 = models.FloatField(blank=True, null=True)
    cnl_042 = models.FloatField(blank=True, null=True)
    cnl_043 = models.FloatField(blank=True, null=True)
    cnl_044 = models.FloatField(blank=True, null=True)
    cnl_045 = models.FloatField(blank=True, null=True)
    cnl_046 = models.FloatField(blank=True, null=True)
    cnl_047 = models.FloatField(blank=True, null=True)
    cnl_048 = models.FloatField(blank=True, null=True)
    cnl_049 = models.FloatField(blank=True, null=True)
    cnl_050 = models.FloatField(blank=True, null=True)
    cnl_051 = models.FloatField(blank=True, null=True)
    cnl_052 = models.FloatField(blank=True, null=True)
    cnl_053 = models.FloatField(blank=True, null=True)
    cnl_054 = models.FloatField(blank=True, null=True)
    cnl_055 = models.FloatField(blank=True, null=True)
    cnl_056 = models.FloatField(blank=True, null=True)
    cnl_057 = models.FloatField(blank=True, null=True)
    cnl_058 = models.FloatField(blank=True, null=True)
    cnl_059 = models.FloatField(blank=True, null=True)
    cnl_060 = models.FloatField(blank=True, null=True)
    cnl_061 = models.FloatField(blank=True, null=True)
    cnl_062 = models.FloatField(blank=True, null=True)
    cnl_063 = models.FloatField(blank=True, null=True)
    cnl_064 = models.FloatField(blank=True, null=True)
    cnl_065 = models.FloatField(blank=True, null=True)
    cnl_066 = models.FloatField(blank=True, null=True)
    cnl_067 = models.FloatField(blank=True, null=True)
    cnl_068 = models.FloatField(blank=True, null=True)
    cnl_069 = models.FloatField(blank=True, null=True)
    cnl_070 = models.FloatField(blank=True, null=True)
    cnl_071 = models.FloatField(blank=True, null=True)
    cnl_072 = models.FloatField(blank=True, null=True)
    cnl_073 = models.FloatField(blank=True, null=True)
    cnl_074 = models.FloatField(blank=True, null=True)
    cnl_075 = models.FloatField(blank=True, null=True)
    cnl_076 = models.FloatField(blank=True, null=True)
    cnl_077 = models.FloatField(blank=True, null=True)
    cnl_078 = models.FloatField(blank=True, null=True)
    cnl_079 = models.FloatField(blank=True, null=True)
    cnl_080 = models.FloatField(blank=True, null=True)
    cnl_081 = models.FloatField(blank=True, null=True)
    cnl_082 = models.FloatField(blank=True, null=True)
    cnl_083 = models.FloatField(blank=True, null=True)
    cnl_084 = models.FloatField(blank=True, null=True)
    cnl_085 = models.FloatField(blank=True, null=True)
    cnl_086 = models.FloatField(blank=True, null=True)
    cnl_087 = models.FloatField(blank=True, null=True)
    cnl_088 = models.FloatField(blank=True, null=True)
    cnl_089 = models.FloatField(blank=True, null=True)
    cnl_090 = models.FloatField(blank=True, null=True)
    cnl_091 = models.FloatField(blank=True, null=True)
    cnl_092 = models.FloatField(blank=True, null=True)
    cnl_093 = models.FloatField(blank=True, null=True)
    cnl_094 = models.FloatField(blank=True, null=True)
    cnl_095 = models.FloatField(blank=True, null=True)
    cnl_096 = models.FloatField(blank=True, null=True)
    cnl_097 = models.FloatField(blank=True, null=True)
    cnl_098 = models.FloatField(blank=True, null=True)
    cnl_099 = models.FloatField(blank=True, null=True)
    cnl_100 = models.FloatField(blank=True, null=True)
    cnl_101 = models.FloatField(blank=True, null=True)
    cnl_102 = models.FloatField(blank=True, null=True)
    cnl_103 = models.FloatField(blank=True, null=True)
    cnl_104 = models.FloatField(blank=True, null=True)
    cnl_105 = models.FloatField(blank=True, null=True)
    cnl_106 = models.FloatField(blank=True, null=True)
    cnl_107 = models.FloatField(blank=True, null=True)
    cnl_108 = models.FloatField(blank=True, null=True)
    cnl_109 = models.FloatField(blank=True, null=True)
    cnl_110 = models.FloatField(blank=True, null=True)
    cnl_111 = models.FloatField(blank=True, null=True)
    cnl_112 = models.FloatField(blank=True, null=True)
    cnl_113 = models.FloatField(blank=True, null=True)
    cnl_114 = models.FloatField(blank=True, null=True)
    cnl_115 = models.FloatField(blank=True, null=True)
    cnl_116 = models.FloatField(blank=True, null=True)
    cnl_117 = models.FloatField(blank=True, null=True)
    cnl_118 = models.FloatField(blank=True, null=True)
    cnl_119 = models.FloatField(blank=True, null=True)
    cnl_120 = models.FloatField(blank=True, null=True)
    cnl_121 = models.FloatField(blank=True, null=True)
    cnl_122 = models.FloatField(blank=True, null=True)
    cnl_123 = models.FloatField(blank=True, null=True)
    cnl_124 = models.FloatField(blank=True, null=True)
    cnl_125 = models.FloatField(blank=True, null=True)
    cnl_126 = models.FloatField(blank=True, null=True)
    cnl_127 = models.FloatField(blank=True, null=True)
    cnl_128 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datas_base_calb_of_mid_range'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Equivalents(models.Model):
    equivalent_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField(blank=True, null=True)
    index_pnt_in_file = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()
    time_in_mjd = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    type_of_equivalent = models.IntegerField(blank=True, null=True)
    scale_in_k_temp = models.FloatField(blank=True, null=True)
    usability = models.FloatField(blank=True, null=True)
    cnl_001 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_002 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_003 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_004 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_005 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_006 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_007 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_008 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_009 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_010 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_011 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_012 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_013 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_014 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_015 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_016 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_017 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_018 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_019 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_020 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_021 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_022 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_023 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_024 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_025 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_026 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_027 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_028 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_029 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_030 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_031 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_032 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_033 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_034 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_035 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_036 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_037 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_038 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_039 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_040 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_041 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_042 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_043 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_044 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_045 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_046 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_047 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_048 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_049 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_050 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_051 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_052 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_053 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_054 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_055 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_056 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_057 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_058 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_059 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_060 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_061 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_062 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_063 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_064 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_065 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_066 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_067 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_068 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_069 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_070 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_071 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_072 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_073 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_074 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_075 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_076 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_077 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_078 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_079 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_080 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_081 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_082 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_083 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_084 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_085 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_086 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_087 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_088 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_089 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_090 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_091 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_092 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_093 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_094 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_095 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_096 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_097 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_098 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_099 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_100 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_101 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_102 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_103 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_104 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_105 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_106 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_107 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_108 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_109 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_110 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_111 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_112 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_113 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_114 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_115 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_116 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_117 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_118 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_119 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_120 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_121 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_122 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_123 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_124 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_125 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_126 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_127 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cnl_128 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'equivalents'


class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_in_mjd_start = models.FloatField(blank=True, null=True)
    time_in_mjd_stop = models.FloatField(blank=True, null=True)
    alpha_start = models.FloatField(blank=True, null=True)
    alpha_stop = models.FloatField(blank=True, null=True)
    time_interval_in_mjd = models.FloatField(blank=True, null=True)
    type_of_image = models.IntegerField(blank=True, null=True)
    cod_interval = models.IntegerField(blank=True, null=True)
    type_of_data = models.IntegerField(blank=True, null=True)
    number_first_channel = models.IntegerField(blank=True, null=True)
    number_last_channel = models.IntegerField(blank=True, null=True)
    version_of_image = models.IntegerField(blank=True, null=True)
    name_file_on_disc = models.CharField(unique=True, max_length=256)
    name_file_in_inet = models.CharField(unique=True, max_length=256)
    name_file_short = models.CharField(unique=True, max_length=128)
    counter_of_image = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'images'


class IpUser(models.Model):
    ip_id = models.AutoField(primary_key=True)
    user_login = models.CharField(max_length=32)
    ip_address = models.GenericIPAddressField()
    counter_of_ip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ip_user'


class ListOfCnlGrid(models.Model):
    list_id = models.AutoField(primary_key=True)
    time_start = models.DateTimeField()
    time_stop = models.DateTimeField()
    type_investigation = models.IntegerField()
    id_number_box_data = models.IntegerField()
    cnl_list = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'list_of_cnl_grid'


class ListOfCoordinateOfCnl(models.Model):
    list_of_coordinate_id = models.AutoField(primary_key=True)
    time_start = models.DateTimeField()
    time_stop = models.DateTimeField()
    cnl_001 = models.FloatField(blank=True, null=True)
    cnl_002 = models.FloatField(blank=True, null=True)
    cnl_003 = models.FloatField(blank=True, null=True)
    cnl_004 = models.FloatField(blank=True, null=True)
    cnl_005 = models.FloatField(blank=True, null=True)
    cnl_006 = models.FloatField(blank=True, null=True)
    cnl_007 = models.FloatField(blank=True, null=True)
    cnl_008 = models.FloatField(blank=True, null=True)
    cnl_009 = models.FloatField(blank=True, null=True)
    cnl_010 = models.FloatField(blank=True, null=True)
    cnl_011 = models.FloatField(blank=True, null=True)
    cnl_012 = models.FloatField(blank=True, null=True)
    cnl_013 = models.FloatField(blank=True, null=True)
    cnl_014 = models.FloatField(blank=True, null=True)
    cnl_015 = models.FloatField(blank=True, null=True)
    cnl_016 = models.FloatField(blank=True, null=True)
    cnl_017 = models.FloatField(blank=True, null=True)
    cnl_018 = models.FloatField(blank=True, null=True)
    cnl_019 = models.FloatField(blank=True, null=True)
    cnl_020 = models.FloatField(blank=True, null=True)
    cnl_021 = models.FloatField(blank=True, null=True)
    cnl_022 = models.FloatField(blank=True, null=True)
    cnl_023 = models.FloatField(blank=True, null=True)
    cnl_024 = models.FloatField(blank=True, null=True)
    cnl_025 = models.FloatField(blank=True, null=True)
    cnl_026 = models.FloatField(blank=True, null=True)
    cnl_027 = models.FloatField(blank=True, null=True)
    cnl_028 = models.FloatField(blank=True, null=True)
    cnl_029 = models.FloatField(blank=True, null=True)
    cnl_030 = models.FloatField(blank=True, null=True)
    cnl_031 = models.FloatField(blank=True, null=True)
    cnl_032 = models.FloatField(blank=True, null=True)
    cnl_033 = models.FloatField(blank=True, null=True)
    cnl_034 = models.FloatField(blank=True, null=True)
    cnl_035 = models.FloatField(blank=True, null=True)
    cnl_036 = models.FloatField(blank=True, null=True)
    cnl_037 = models.FloatField(blank=True, null=True)
    cnl_038 = models.FloatField(blank=True, null=True)
    cnl_039 = models.FloatField(blank=True, null=True)
    cnl_040 = models.FloatField(blank=True, null=True)
    cnl_041 = models.FloatField(blank=True, null=True)
    cnl_042 = models.FloatField(blank=True, null=True)
    cnl_043 = models.FloatField(blank=True, null=True)
    cnl_044 = models.FloatField(blank=True, null=True)
    cnl_045 = models.FloatField(blank=True, null=True)
    cnl_046 = models.FloatField(blank=True, null=True)
    cnl_047 = models.FloatField(blank=True, null=True)
    cnl_048 = models.FloatField(blank=True, null=True)
    cnl_049 = models.FloatField(blank=True, null=True)
    cnl_050 = models.FloatField(blank=True, null=True)
    cnl_051 = models.FloatField(blank=True, null=True)
    cnl_052 = models.FloatField(blank=True, null=True)
    cnl_053 = models.FloatField(blank=True, null=True)
    cnl_054 = models.FloatField(blank=True, null=True)
    cnl_055 = models.FloatField(blank=True, null=True)
    cnl_056 = models.FloatField(blank=True, null=True)
    cnl_057 = models.FloatField(blank=True, null=True)
    cnl_058 = models.FloatField(blank=True, null=True)
    cnl_059 = models.FloatField(blank=True, null=True)
    cnl_060 = models.FloatField(blank=True, null=True)
    cnl_061 = models.FloatField(blank=True, null=True)
    cnl_062 = models.FloatField(blank=True, null=True)
    cnl_063 = models.FloatField(blank=True, null=True)
    cnl_064 = models.FloatField(blank=True, null=True)
    cnl_065 = models.FloatField(blank=True, null=True)
    cnl_066 = models.FloatField(blank=True, null=True)
    cnl_067 = models.FloatField(blank=True, null=True)
    cnl_068 = models.FloatField(blank=True, null=True)
    cnl_069 = models.FloatField(blank=True, null=True)
    cnl_070 = models.FloatField(blank=True, null=True)
    cnl_071 = models.FloatField(blank=True, null=True)
    cnl_072 = models.FloatField(blank=True, null=True)
    cnl_073 = models.FloatField(blank=True, null=True)
    cnl_074 = models.FloatField(blank=True, null=True)
    cnl_075 = models.FloatField(blank=True, null=True)
    cnl_076 = models.FloatField(blank=True, null=True)
    cnl_077 = models.FloatField(blank=True, null=True)
    cnl_078 = models.FloatField(blank=True, null=True)
    cnl_079 = models.FloatField(blank=True, null=True)
    cnl_080 = models.FloatField(blank=True, null=True)
    cnl_081 = models.FloatField(blank=True, null=True)
    cnl_082 = models.FloatField(blank=True, null=True)
    cnl_083 = models.FloatField(blank=True, null=True)
    cnl_084 = models.FloatField(blank=True, null=True)
    cnl_085 = models.FloatField(blank=True, null=True)
    cnl_086 = models.FloatField(blank=True, null=True)
    cnl_087 = models.FloatField(blank=True, null=True)
    cnl_088 = models.FloatField(blank=True, null=True)
    cnl_089 = models.FloatField(blank=True, null=True)
    cnl_090 = models.FloatField(blank=True, null=True)
    cnl_091 = models.FloatField(blank=True, null=True)
    cnl_092 = models.FloatField(blank=True, null=True)
    cnl_093 = models.FloatField(blank=True, null=True)
    cnl_094 = models.FloatField(blank=True, null=True)
    cnl_095 = models.FloatField(blank=True, null=True)
    cnl_096 = models.FloatField(blank=True, null=True)
    cnl_097 = models.FloatField(blank=True, null=True)
    cnl_098 = models.FloatField(blank=True, null=True)
    cnl_099 = models.FloatField(blank=True, null=True)
    cnl_100 = models.FloatField(blank=True, null=True)
    cnl_101 = models.FloatField(blank=True, null=True)
    cnl_102 = models.FloatField(blank=True, null=True)
    cnl_103 = models.FloatField(blank=True, null=True)
    cnl_104 = models.FloatField(blank=True, null=True)
    cnl_105 = models.FloatField(blank=True, null=True)
    cnl_106 = models.FloatField(blank=True, null=True)
    cnl_107 = models.FloatField(blank=True, null=True)
    cnl_108 = models.FloatField(blank=True, null=True)
    cnl_109 = models.FloatField(blank=True, null=True)
    cnl_110 = models.FloatField(blank=True, null=True)
    cnl_111 = models.FloatField(blank=True, null=True)
    cnl_112 = models.FloatField(blank=True, null=True)
    cnl_113 = models.FloatField(blank=True, null=True)
    cnl_114 = models.FloatField(blank=True, null=True)
    cnl_115 = models.FloatField(blank=True, null=True)
    cnl_116 = models.FloatField(blank=True, null=True)
    cnl_117 = models.FloatField(blank=True, null=True)
    cnl_118 = models.FloatField(blank=True, null=True)
    cnl_119 = models.FloatField(blank=True, null=True)
    cnl_120 = models.FloatField(blank=True, null=True)
    cnl_121 = models.FloatField(blank=True, null=True)
    cnl_122 = models.FloatField(blank=True, null=True)
    cnl_123 = models.FloatField(blank=True, null=True)
    cnl_124 = models.FloatField(blank=True, null=True)
    cnl_125 = models.FloatField(blank=True, null=True)
    cnl_126 = models.FloatField(blank=True, null=True)
    cnl_127 = models.FloatField(blank=True, null=True)
    cnl_128 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list_of_coordinate_of_cnl'


class NameFiles(models.Model):
    files_id = models.AutoField(primary_key=True)
    name_file_of_datas = models.CharField(unique=True, max_length=256)
    name_file_short = models.CharField(max_length=256)
    fsize = models.BigIntegerField()
    type_investigation = models.IntegerField()
    id_number_box_data = models.IntegerField(blank=True, null=True)
    modulus = models.CharField(max_length=32, blank=True, null=True)
    time_start = models.DateTimeField()
    time_stop = models.DateTimeField()
    time_start_in_mjd = models.FloatField(blank=True, null=True)
    fcentral = models.FloatField(blank=True, null=True)
    wb_total = models.FloatField(blank=True, null=True)
    tresolution = models.FloatField(blank=True, null=True)
    npoints = models.IntegerField(blank=True, null=True)
    nbands = models.IntegerField(blank=True, null=True)
    wbands = models.TextField(blank=True, null=True)  # This field type is a guess.
    fbands = models.TextField(blank=True, null=True)  # This field type is a guess.
    quality_of_datas = models.TextField(blank=True, null=True)  # This field type is a guess.
    usability = models.FloatField(blank=True, null=True)
    alpha_begin = models.FloatField(blank=True, null=True)
    alpha_end = models.FloatField(blank=True, null=True)
    delta_begin = models.FloatField(blank=True, null=True)
    delta_end = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'name_files'
# Unable to inspect table 'reflection'
# The error was: permission denied for relation reflection



class SkyObjects(models.Model):
    sky_objects_id = models.AutoField(primary_key=True)
    files_id = models.IntegerField(blank=True, null=True)
    index_pnt_in_file = models.IntegerField(blank=True, null=True)
    tested = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    type_objects = models.IntegerField(blank=True, null=True)
    name_objects = models.CharField(max_length=32, blank=True, null=True)
    nbands = models.IntegerField(blank=True, null=True)
    s_n_bands = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_n_total = models.FloatField(blank=True, null=True)
    tresolution = models.FloatField(blank=True, null=True)
    width_obj = models.FloatField(blank=True, null=True)
    max_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    median_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    deviation_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    parameters = models.TextField(blank=True, null=True)  # This field type is a guess.
    time = models.DateTimeField()
    time_in_mjd = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    delta = models.FloatField(blank=True, null=True)
    cnl = models.IntegerField(blank=True, null=True)
    name_cnl = models.CharField(max_length=8)
    npoints_in_arr = models.IntegerField(blank=True, null=True)
    array_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    param_int = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sky_objects'


class Weather(models.Model):
    weather_id = models.AutoField(primary_key=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_in_mjd_stop = models.FloatField(blank=True, null=True)
    alpha_stop = models.FloatField(blank=True, null=True)
    temperature_c = models.FloatField(blank=True, null=True)
    thw_index = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    rain = models.FloatField(blank=True, null=True)
    hi_rain = models.FloatField(blank=True, null=True)
    bar = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_dir = models.CharField(max_length=4, blank=True, null=True)
    type_of_data = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather'
