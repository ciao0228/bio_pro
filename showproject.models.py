# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataEvent(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_event'


class DataOffline(models.Model):
    upload = models.PositiveIntegerField(db_column='UPLOAD')  # Field name made lowercase.
    project = models.ForeignKey('DataProject', models.DO_NOTHING, db_column='PROJECT_ID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relativetime = models.PositiveIntegerField(db_column='RELATIVETIME')  # Field name made lowercase.
    sample_time = models.DateTimeField(db_column='SAMPLE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_flag = models.IntegerField(db_column='UPDATE_FLAG', blank=True, null=True)  # Field name made lowercase.
    p1 = models.FloatField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.FloatField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    ph2 = models.FloatField(db_column='PH2', blank=True, null=True)  # Field name made lowercase.
    poff = models.FloatField(db_column='POFF', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    nh2n = models.FloatField(db_column='NH2N', blank=True, null=True)  # Field name made lowercase.
    foff = models.FloatField(db_column='FOFF', blank=True, null=True)  # Field name made lowercase.
    voff = models.FloatField(db_column='VOFF', blank=True, null=True)  # Field name made lowercase.
    s1 = models.FloatField(db_column='S1', blank=True, null=True)  # Field name made lowercase.
    s2 = models.FloatField(db_column='S2', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.
    r3 = models.FloatField(db_column='R3', blank=True, null=True)  # Field name made lowercase.
    r4 = models.FloatField(db_column='R4', blank=True, null=True)  # Field name made lowercase.
    r5 = models.FloatField(db_column='R5', blank=True, null=True)  # Field name made lowercase.
    r6 = models.FloatField(db_column='R6', blank=True, null=True)  # Field name made lowercase.
    mu = models.FloatField(db_column='MU', blank=True, null=True)  # Field name made lowercase.
    rp1 = models.FloatField(db_column='RP1', blank=True, null=True)  # Field name made lowercase.
    rp2 = models.FloatField(db_column='RP2', blank=True, null=True)  # Field name made lowercase.
    rs1 = models.FloatField(db_column='RS1', blank=True, null=True)  # Field name made lowercase.
    rs2 = models.FloatField(db_column='RS2', blank=True, null=True)  # Field name made lowercase.
    offcalc1 = models.FloatField(db_column='OFFCALC1', blank=True, null=True)  # Field name made lowercase.
    offcalc2 = models.FloatField(db_column='OFFCALC2', blank=True, null=True)  # Field name made lowercase.
    offcalc3 = models.FloatField(db_column='OFFCALC3', blank=True, null=True)  # Field name made lowercase.
    offcalc4 = models.FloatField(db_column='OFFCALC4', blank=True, null=True)  # Field name made lowercase.
    offcalc5 = models.FloatField(db_column='OFFCALC5', blank=True, null=True)  # Field name made lowercase.
    offcalc6 = models.FloatField(db_column='OFFCALC6', blank=True, null=True)  # Field name made lowercase.
    offcalc7 = models.FloatField(db_column='OFFCALC7', blank=True, null=True)  # Field name made lowercase.
    offcalc8 = models.FloatField(db_column='OFFCALC8', blank=True, null=True)  # Field name made lowercase.
    offcalc9 = models.FloatField(db_column='OFFCALC9', blank=True, null=True)  # Field name made lowercase.
    offcalc10 = models.FloatField(db_column='OFFCALC10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_offline'


class DataOnline(models.Model):
    upload = models.PositiveIntegerField(db_column='UPLOAD')  # Field name made lowercase.
    project = models.ForeignKey('DataProject', models.DO_NOTHING, db_column='PROJECT_ID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relativetime = models.PositiveIntegerField(db_column='RELATIVETIME')  # Field name made lowercase.
    sample_time = models.DateTimeField(db_column='SAMPLE_TIME')  # Field name made lowercase.
    update_flag = models.IntegerField(db_column='UPDATE_FLAG', blank=True, null=True)  # Field name made lowercase.
    temp = models.FloatField(db_column='TEMP', blank=True, null=True)  # Field name made lowercase.
    f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    ado = models.FloatField(db_column='ADO', blank=True, null=True)  # Field name made lowercase.
    ph1 = models.FloatField(db_column='PH1', blank=True, null=True)  # Field name made lowercase.
    v = models.FloatField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    eo2 = models.FloatField(db_column='EO2', blank=True, null=True)  # Field name made lowercase.
    eco2 = models.FloatField(db_column='ECO2', blank=True, null=True)  # Field name made lowercase.
    rpm = models.FloatField(db_column='RPM', blank=True, null=True)  # Field name made lowercase.
    od1 = models.FloatField(db_column='OD1', blank=True, null=True)  # Field name made lowercase.
    af1 = models.FloatField(db_column='AF1', blank=True, null=True)  # Field name made lowercase.
    af2 = models.FloatField(db_column='AF2', blank=True, null=True)  # Field name made lowercase.
    af3 = models.FloatField(db_column='AF3', blank=True, null=True)  # Field name made lowercase.
    rf1 = models.FloatField(db_column='RF1', blank=True, null=True)  # Field name made lowercase.
    rf2 = models.FloatField(db_column='RF2', blank=True, null=True)  # Field name made lowercase.
    rf3 = models.FloatField(db_column='RF3', blank=True, null=True)  # Field name made lowercase.
    p = models.FloatField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    af4 = models.FloatField(db_column='AF4', blank=True, null=True)  # Field name made lowercase.
    af5 = models.FloatField(db_column='AF5', blank=True, null=True)  # Field name made lowercase.
    af6 = models.FloatField(db_column='AF6', blank=True, null=True)  # Field name made lowercase.
    rf4 = models.FloatField(db_column='RF4', blank=True, null=True)  # Field name made lowercase.
    rf5 = models.FloatField(db_column='RF5', blank=True, null=True)  # Field name made lowercase.
    rf6 = models.FloatField(db_column='RF6', blank=True, null=True)  # Field name made lowercase.
    onr1 = models.FloatField(db_column='ONR1', blank=True, null=True)  # Field name made lowercase.
    onr2 = models.FloatField(db_column='ONR2', blank=True, null=True)  # Field name made lowercase.
    onr3 = models.FloatField(db_column='ONR3', blank=True, null=True)  # Field name made lowercase.
    onr4 = models.FloatField(db_column='ONR4', blank=True, null=True)  # Field name made lowercase.
    onr5 = models.FloatField(db_column='ONR5', blank=True, null=True)  # Field name made lowercase.
    onr6 = models.FloatField(db_column='ONR6', blank=True, null=True)  # Field name made lowercase.
    onr7 = models.FloatField(db_column='ONR7', blank=True, null=True)  # Field name made lowercase.
    onr8 = models.FloatField(db_column='ONR8', blank=True, null=True)  # Field name made lowercase.
    onr9 = models.FloatField(db_column='ONR9', blank=True, null=True)  # Field name made lowercase.
    onr10 = models.FloatField(db_column='ONR10', blank=True, null=True)  # Field name made lowercase.
    onr11 = models.FloatField(db_column='ONR11', blank=True, null=True)  # Field name made lowercase.
    onr12 = models.FloatField(db_column='ONR12', blank=True, null=True)  # Field name made lowercase.
    onr13 = models.FloatField(db_column='ONR13', blank=True, null=True)  # Field name made lowercase.
    onr14 = models.FloatField(db_column='ONR14', blank=True, null=True)  # Field name made lowercase.
    onr15 = models.FloatField(db_column='ONR15', blank=True, null=True)  # Field name made lowercase.
    onr16 = models.FloatField(db_column='ONR16', blank=True, null=True)  # Field name made lowercase.
    onr17 = models.FloatField(db_column='ONR17', blank=True, null=True)  # Field name made lowercase.
    onr18 = models.FloatField(db_column='ONR18', blank=True, null=True)  # Field name made lowercase.
    onr19 = models.FloatField(db_column='ONR19', blank=True, null=True)  # Field name made lowercase.
    onr20 = models.FloatField(db_column='ONR20', blank=True, null=True)  # Field name made lowercase.
    our = models.FloatField(db_column='OUR', blank=True, null=True)  # Field name made lowercase.
    cer = models.FloatField(db_column='CER', blank=True, null=True)  # Field name made lowercase.
    rq = models.FloatField(db_column='RQ', blank=True, null=True)  # Field name made lowercase.
    kla = models.FloatField(db_column='KLA', blank=True, null=True)  # Field name made lowercase.
    oncalc1 = models.FloatField(db_column='ONCALC1', blank=True, null=True)  # Field name made lowercase.
    oncalc2 = models.FloatField(db_column='ONCALC2', blank=True, null=True)  # Field name made lowercase.
    oncalc3 = models.FloatField(db_column='ONCALC3', blank=True, null=True)  # Field name made lowercase.
    oncalc4 = models.FloatField(db_column='ONCALC4', blank=True, null=True)  # Field name made lowercase.
    oncalc5 = models.FloatField(db_column='ONCALC5', blank=True, null=True)  # Field name made lowercase.
    oncalc6 = models.FloatField(db_column='ONCALC6', blank=True, null=True)  # Field name made lowercase.
    oncalc7 = models.FloatField(db_column='ONCALC7', blank=True, null=True)  # Field name made lowercase.
    oncalc8 = models.FloatField(db_column='ONCALC8', blank=True, null=True)  # Field name made lowercase.
    oncalc9 = models.FloatField(db_column='ONCALC9', blank=True, null=True)  # Field name made lowercase.
    oncalc10 = models.FloatField(db_column='ONCALC10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_online'


class DataProject(models.Model):
    upload = models.PositiveIntegerField(db_column='UPLOAD')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    update_flag = models.IntegerField(db_column='UPDATE_FLAG', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='TEXT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ainfo = models.TextField(db_column='AINFO', blank=True, null=True)  # Field name made lowercase.
    acomment = models.TextField(db_column='ACOMMENT', blank=True, null=True)  # Field name made lowercase.
    begin_time = models.DateTimeField(db_column='BEGIN_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_project'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoApschedulerDjangojob(models.Model):
    name = models.CharField(unique=True, max_length=255)
    next_run_time = models.DateTimeField(blank=True, null=True)
    job_state = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojob'


class DjangoApschedulerDjangojobexecution(models.Model):
    status = models.CharField(max_length=50)
    run_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    started = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    finished = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    exception = models.CharField(max_length=1000, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    job = models.ForeignKey(DjangoApschedulerDjangojob, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojobexecution'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OffRange(models.Model):
    chars = models.CharField(max_length=255, blank=True, null=True)
    meaning = models.CharField(max_length=255, blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'off_range'


class OnRange(models.Model):
    chars = models.CharField(max_length=255, blank=True, null=True)
    meaning = models.CharField(max_length=255, blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'on_range'


class User1(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user1'
