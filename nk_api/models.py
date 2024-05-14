from django.db import models

# Create your models here.
class Api(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nk_tb_crmAPI'
    
    def __str__(self):
        return self.nombre
class Art(models.Model):
    articulo = models.CharField(db_column='Articulo', primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rama = models.CharField(db_column='Rama', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcion1 = models.CharField(db_column='Descripcion1', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcion2 = models.CharField(db_column='Descripcion2', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombrecorto = models.CharField(db_column='NombreCorto', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoriaactivofijo = models.CharField(db_column='CategoriaActivoFijo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    linea = models.CharField(db_column='Linea', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fabricante = models.CharField(db_column='Fabricante', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clavefabricante = models.CharField(db_column='ClaveFabricante', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    impuesto1 = models.FloatField(db_column='Impuesto1')  # Field name made lowercase.
    impuesto2 = models.FloatField(db_column='Impuesto2', blank=True, null=True)  # Field name made lowercase.
    impuesto3 = models.FloatField(db_column='Impuesto3', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unidadcompra = models.CharField(db_column='UnidadCompra', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unidadtraspaso = models.CharField(db_column='UnidadTraspaso', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unidadcantidad = models.FloatField(db_column='UnidadCantidad', blank=True, null=True)  # Field name made lowercase.
    tipocosteo = models.CharField(db_column='TipoCosteo', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='Peso', blank=True, null=True)  # Field name made lowercase.
    tara = models.FloatField(db_column='Tara', blank=True, null=True)  # Field name made lowercase.
    volumen = models.FloatField(db_column='Volumen', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tipoopcion = models.CharField(db_column='TipoOpcion', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    accesorios = models.BooleanField(db_column='Accesorios')  # Field name made lowercase.
    refacciones = models.BooleanField(db_column='Refacciones')  # Field name made lowercase.
    sustitutos = models.BooleanField(db_column='Sustitutos')  # Field name made lowercase.
    servicios = models.BooleanField(db_column='Servicios', blank=True, null=True)  # Field name made lowercase.
    consumibles = models.BooleanField(db_column='Consumibles', blank=True, null=True)  # Field name made lowercase.
    monedacosto = models.CharField(db_column='MonedaCosto', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    monedaprecio = models.CharField(db_column='MonedaPrecio', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    margenminimo = models.DecimalField(db_column='MargenMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciolista = models.DecimalField(db_column='PrecioLista', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciominimo = models.DecimalField(db_column='PrecioMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    factoralterno = models.FloatField(db_column='FactorAlterno', blank=True, null=True)  # Field name made lowercase.
    precioanterior = models.DecimalField(db_column='PrecioAnterior', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    utilidad = models.CharField(db_column='Utilidad', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descuentocompra = models.FloatField(db_column='DescuentoCompra', blank=True, null=True)  # Field name made lowercase.
    clase = models.CharField(db_column='Clase', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ultimocambio = models.DateTimeField(db_column='UltimoCambio', blank=True, null=True)  # Field name made lowercase.
    alta = models.DateTimeField(db_column='Alta', blank=True, null=True)  # Field name made lowercase.
    conciliar = models.BooleanField(db_column='Conciliar')  # Field name made lowercase.
    mensaje = models.CharField(db_column='Mensaje', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comision = models.CharField(db_column='Comision', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    arancel = models.CharField(db_column='Arancel', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aranceldesperdicio = models.CharField(db_column='ArancelDesperdicio', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    abc = models.CharField(db_column='ABC', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    precio2 = models.DecimalField(db_column='Precio2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio3 = models.DecimalField(db_column='Precio3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio4 = models.DecimalField(db_column='Precio4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio5 = models.DecimalField(db_column='Precio5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio6 = models.DecimalField(db_column='Precio6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio7 = models.DecimalField(db_column='Precio7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio8 = models.DecimalField(db_column='Precio8', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio9 = models.DecimalField(db_column='Precio9', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio10 = models.DecimalField(db_column='Precio10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    refrigeracion = models.BooleanField(db_column='Refrigeracion')  # Field name made lowercase.
    tienecaducidad = models.BooleanField(db_column='TieneCaducidad')  # Field name made lowercase.
    basculapesar = models.BooleanField(db_column='BasculaPesar', blank=True, null=True)  # Field name made lowercase.
    seproduce = models.BooleanField(db_column='SeProduce')  # Field name made lowercase.
    situacion = models.CharField(db_column='Situacion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacionfecha = models.DateTimeField(db_column='SituacionFecha', blank=True, null=True)  # Field name made lowercase.
    situacionusuario = models.CharField(db_column='SituacionUsuario', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    situacionnota = models.CharField(db_column='SituacionNota', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estatusprecio = models.CharField(db_column='EstatusPrecio', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wmostrar = models.BooleanField(db_column='wMostrar', blank=True, null=True)  # Field name made lowercase.
    merma = models.FloatField(db_column='Merma', blank=True, null=True)  # Field name made lowercase.
    desperdicio = models.FloatField(db_column='Desperdicio', blank=True, null=True)  # Field name made lowercase.
    secompra = models.BooleanField(db_column='SeCompra', blank=True, null=True)  # Field name made lowercase.
    sevende = models.BooleanField(db_column='SeVende', blank=True, null=True)  # Field name made lowercase.
    esformula = models.BooleanField(db_column='EsFormula', blank=True, null=True)  # Field name made lowercase.
    tiempoentrega = models.IntegerField(db_column='TiempoEntrega', blank=True, null=True)  # Field name made lowercase.
    tiempoentregaunidad = models.CharField(db_column='TiempoEntregaUnidad', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tiempoentregaseg = models.IntegerField(db_column='TiempoEntregaSeg', blank=True, null=True)  # Field name made lowercase.
    tiempoentregasegunidad = models.CharField(db_column='TiempoEntregaSegUnidad', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loteordenar = models.CharField(db_column='LoteOrdenar', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cantidadordenar = models.FloatField(db_column='CantidadOrdenar', blank=True, null=True)  # Field name made lowercase.
    multiplosordenar = models.FloatField(db_column='MultiplosOrdenar', blank=True, null=True)  # Field name made lowercase.
    invseguridad = models.FloatField(db_column='InvSeguridad', blank=True, null=True)  # Field name made lowercase.
    prodruta = models.CharField(db_column='ProdRuta', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    almacenrop = models.CharField(db_column='AlmacenROP', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoriaprod = models.CharField(db_column='CategoriaProd', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodcantidad = models.FloatField(db_column='ProdCantidad', blank=True, null=True)  # Field name made lowercase.
    produsuario = models.CharField(db_column='ProdUsuario', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodpasototal = models.IntegerField(db_column='ProdPasoTotal', blank=True, null=True)  # Field name made lowercase.
    prodmovgrupo = models.CharField(db_column='ProdMovGrupo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodestacion = models.CharField(db_column='ProdEstacion', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodopciones = models.BooleanField(db_column='ProdOpciones')  # Field name made lowercase.
    prodverconcentracion = models.BooleanField(db_column='ProdVerConcentracion', blank=True, null=True)  # Field name made lowercase.
    prodvercostoacumulado = models.BooleanField(db_column='ProdVerCostoAcumulado', blank=True, null=True)  # Field name made lowercase.
    prodvermerma = models.BooleanField(db_column='ProdVerMerma', blank=True, null=True)  # Field name made lowercase.
    prodverdesperdicio = models.BooleanField(db_column='ProdVerDesperdicio', blank=True, null=True)  # Field name made lowercase.
    prodverporcentaje = models.BooleanField(db_column='ProdVerPorcentaje', blank=True, null=True)  # Field name made lowercase.
    revisionultima = models.DateTimeField(db_column='RevisionUltima', blank=True, null=True)  # Field name made lowercase.
    revisionusuario = models.CharField(db_column='RevisionUsuario', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    revisionfrecuencia = models.IntegerField(db_column='RevisionFrecuencia', blank=True, null=True)  # Field name made lowercase.
    revisionfrecuenciaunidad = models.CharField(db_column='RevisionFrecuenciaUnidad', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    revisionsiguiente = models.DateTimeField(db_column='RevisionSiguiente', blank=True, null=True)  # Field name made lowercase.
    prodmov = models.CharField(db_column='ProdMov', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipocompra = models.CharField(db_column='TipoCompra', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tienemovimientos = models.BooleanField(db_column='TieneMovimientos', blank=True, null=True)  # Field name made lowercase.
    registro1 = models.CharField(db_column='Registro1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    registro1vencimiento = models.DateTimeField(db_column='Registro1Vencimiento', blank=True, null=True)  # Field name made lowercase.
    almacenespecificoventa = models.CharField(db_column='AlmacenEspecificoVenta', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    almacenespecificoventamov = models.CharField(db_column='AlmacenEspecificoVentaMov', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rutadistribucion = models.CharField(db_column='RutaDistribucion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    costoestandar = models.FloatField(db_column='CostoEstandar', blank=True, null=True)  # Field name made lowercase.
    costoreposicion = models.FloatField(db_column='CostoReposicion', blank=True, null=True)  # Field name made lowercase.
    estatuscosto = models.CharField(db_column='EstatusCosto', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    margen = models.DecimalField(db_column='Margen', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    proveedor = models.CharField(db_column='Proveedor', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nivelacceso = models.CharField(db_column='NivelAcceso', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    temporada = models.CharField(db_column='Temporada', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    solicitarprecios = models.BooleanField(db_column='SolicitarPrecios', blank=True, null=True)  # Field name made lowercase.
    autorecaudacion = models.CharField(db_column='AutoRecaudacion', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    retencion1 = models.FloatField(db_column='Retencion1', blank=True, null=True)  # Field name made lowercase.
    retencion2 = models.FloatField(db_column='Retencion2', blank=True, null=True)  # Field name made lowercase.
    retencion3 = models.FloatField(db_column='Retencion3', blank=True, null=True)  # Field name made lowercase.
    espacios = models.BooleanField(db_column='Espacios', blank=True, null=True)  # Field name made lowercase.
    espaciosespecificos = models.BooleanField(db_column='EspaciosEspecificos', blank=True, null=True)  # Field name made lowercase.
    espaciossobreventa = models.FloatField(db_column='EspaciosSobreventa', blank=True, null=True)  # Field name made lowercase.
    espaciosnivel = models.CharField(db_column='EspaciosNivel', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    espaciosminutos = models.IntegerField(db_column='EspaciosMinutos', blank=True, null=True)  # Field name made lowercase.
    espaciosbloquearanteriores = models.BooleanField(db_column='EspaciosBloquearAnteriores', blank=True, null=True)  # Field name made lowercase.
    espacioshorad = models.CharField(db_column='EspaciosHoraD', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    espacioshoraa = models.CharField(db_column='EspaciosHoraA', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    serieloteinfo = models.BooleanField(db_column='SerieLoteInfo', blank=True, null=True)  # Field name made lowercase.
    cantidadminimaventa = models.FloatField(db_column='CantidadMinimaVenta', blank=True, null=True)  # Field name made lowercase.
    cantidadmaximaventa = models.FloatField(db_column='CantidadMaximaVenta', blank=True, null=True)  # Field name made lowercase.
    estimulofiscal = models.FloatField(db_column='EstimuloFiscal', blank=True, null=True)  # Field name made lowercase.
    origenpais = models.CharField(db_column='OrigenPais', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    origenlocalidad = models.CharField(db_column='OrigenLocalidad', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    incentivo = models.DecimalField(db_column='Incentivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    factorcompra = models.FloatField(db_column='FactorCompra', blank=True, null=True)  # Field name made lowercase.
    horas = models.FloatField(db_column='Horas', blank=True, null=True)  # Field name made lowercase.
    isan = models.BooleanField(db_column='ISAN', blank=True, null=True)  # Field name made lowercase.
    excluirdescformapago = models.BooleanField(db_column='ExcluirDescFormaPago', blank=True, null=True)  # Field name made lowercase.
    esdeducible = models.BooleanField(db_column='EsDeducible', blank=True, null=True)  # Field name made lowercase.
    peaje = models.DecimalField(db_column='Peaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codigoalterno = models.CharField(db_column='CodigoAlterno', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipocatalogo = models.CharField(db_column='TipoCatalogo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    anexosalfacturar = models.BooleanField(db_column='AnexosAlFacturar', blank=True, null=True)  # Field name made lowercase.
    caducidadminima = models.IntegerField(db_column='CaducidadMinima', blank=True, null=True)  # Field name made lowercase.
    actividades = models.BooleanField(db_column='Actividades', blank=True, null=True)  # Field name made lowercase.
    validarpresupuestocompra = models.CharField(db_column='ValidarPresupuestoCompra', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    serieslotesautoorden = models.CharField(db_column='SeriesLotesAutoOrden', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lotesfijos = models.BooleanField(db_column='LotesFijos', blank=True, null=True)  # Field name made lowercase.
    lotesauto = models.BooleanField(db_column='LotesAuto', blank=True, null=True)  # Field name made lowercase.
    consecutivo = models.IntegerField(db_column='Consecutivo', blank=True, null=True)  # Field name made lowercase.
    tipoempaque = models.CharField(db_column='TipoEmpaque', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tienedireccion = models.BooleanField(db_column='TieneDireccion', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccionnumero = models.CharField(db_column='DireccionNumero', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccionnumeroint = models.CharField(db_column='DireccionNumeroInt', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    entrecalles = models.CharField(db_column='EntreCalles', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plano = models.CharField(db_column='Plano', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='Colonia', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    delegacion = models.CharField(db_column='Delegacion', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    poblacion = models.CharField(db_column='Poblacion', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ruta = models.CharField(db_column='Ruta', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clavevehicular = models.CharField(db_column='ClaveVehicular', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipovehiculo = models.CharField(db_column='TipoVehiculo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diaslibresintereses = models.IntegerField(db_column='DiasLibresIntereses', blank=True, null=True)  # Field name made lowercase.
    precioliberado = models.BooleanField(db_column='PrecioLiberado', blank=True, null=True)  # Field name made lowercase.
    validarcodigo = models.BooleanField(db_column='ValidarCodigo', blank=True, null=True)  # Field name made lowercase.
    presentacion = models.CharField(db_column='Presentacion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    garantiaplazo = models.IntegerField(db_column='GarantiaPlazo', blank=True, null=True)  # Field name made lowercase.
    costoidentificado = models.BooleanField(db_column='CostoIdentificado', blank=True, null=True)  # Field name made lowercase.
    cantidadtarima = models.FloatField(db_column='CantidadTarima', blank=True, null=True)  # Field name made lowercase.
    unidadtarima = models.CharField(db_column='UnidadTarima', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    minimotarima = models.FloatField(db_column='MinimoTarima', blank=True, null=True)  # Field name made lowercase.
    departamentodetallista = models.IntegerField(db_column='DepartamentoDetallista', blank=True, null=True)  # Field name made lowercase.
    tratadocomercial = models.CharField(db_column='TratadoComercial', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cuentapresupuesto = models.CharField(db_column='CuentaPresupuesto', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    programasectorial = models.CharField(db_column='ProgramaSectorial', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedimentoclave = models.CharField(db_column='PedimentoClave', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pedimentoregimen = models.CharField(db_column='PedimentoRegimen', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permiso = models.CharField(db_column='Permiso', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permisorenglon = models.CharField(db_column='PermisoRenglon', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cuenta2 = models.CharField(db_column='Cuenta2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cuenta3 = models.CharField(db_column='Cuenta3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    impuesto1excento = models.BooleanField(db_column='Impuesto1Excento', blank=True, null=True)  # Field name made lowercase.
    calcularpresupuesto = models.BooleanField(db_column='CalcularPresupuesto', blank=True, null=True)  # Field name made lowercase.
    inflacionpresupuesto = models.FloatField(db_column='InflacionPresupuesto', blank=True, null=True)  # Field name made lowercase.
    excento2 = models.BooleanField(db_column='Excento2', blank=True, null=True)  # Field name made lowercase.
    excento3 = models.BooleanField(db_column='Excento3', blank=True, null=True)  # Field name made lowercase.
    contuso = models.CharField(db_column='ContUso', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contuso2 = models.CharField(db_column='ContUso2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contuso3 = models.CharField(db_column='ContUso3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    niveltoleranciacosto = models.CharField(db_column='NivelToleranciaCosto', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    toleranciacosto = models.DecimalField(db_column='ToleranciaCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    toleranciacostoinferior = models.DecimalField(db_column='ToleranciaCostoInferior', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    objetogasto = models.CharField(db_column='ObjetoGasto', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    objetogastoref = models.CharField(db_column='ObjetoGastoRef', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clavepresupuestalimpuesto1 = models.CharField(db_column='ClavePresupuestalImpuesto1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clavepresupuestalretencion1 = models.CharField(db_column='ClavePresupuestalRetencion1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estructura = models.CharField(db_column='Estructura', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoimpuesto1 = models.CharField(db_column='TipoImpuesto1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoimpuesto2 = models.CharField(db_column='TipoImpuesto2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoimpuesto3 = models.CharField(db_column='TipoImpuesto3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoimpuesto4 = models.CharField(db_column='TipoImpuesto4', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoimpuesto5 = models.CharField(db_column='TipoImpuesto5', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tiporetencion1 = models.CharField(db_column='TipoRetencion1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tiporetencion2 = models.CharField(db_column='TipoRetencion2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tiporetencion3 = models.CharField(db_column='TipoRetencion3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saux = models.BooleanField(db_column='SAUX', blank=True, null=True)  # Field name made lowercase.
    inforclaveprincipal = models.CharField(db_column='INFORClavePrincipal', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inforstockminimo = models.FloatField(db_column='INFORStockMinimo', blank=True, null=True)  # Field name made lowercase.
    inforstockmaximo = models.FloatField(db_column='INFORStockMaximo', blank=True, null=True)  # Field name made lowercase.
    inforprefijo = models.CharField(db_column='INFORPrefijo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inforsufijo = models.CharField(db_column='INFORSufijo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codigoestructura = models.CharField(db_column='CodigoEstructura', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipovariante = models.CharField(db_column='TipoVariante', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    infortipo = models.CharField(db_column='INFORTipo', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inforcuarentena = models.IntegerField(db_column='INFORCuarentena', blank=True, null=True)  # Field name made lowercase.
    inforclaveplanta = models.CharField(db_column='INFORClavePlanta', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    infortrazabilidad = models.BooleanField(db_column='INFORTrazabilidad', blank=True, null=True)  # Field name made lowercase.
    inforlotificacionpropia = models.BooleanField(db_column='INFORLotificacionPropia', blank=True, null=True)  # Field name made lowercase.
    inforultimonumerolote = models.IntegerField(db_column='INFORUltimoNumeroLote', blank=True, null=True)  # Field name made lowercase.
    inforunidadesmaximalote = models.IntegerField(db_column='INFORUnidadesMaximaLote', blank=True, null=True)  # Field name made lowercase.
    infortienenoserie = models.BooleanField(db_column='INFORTieneNoSerie', blank=True, null=True)  # Field name made lowercase.
    inforsmr = models.FloatField(db_column='INFORSMR', blank=True, null=True)  # Field name made lowercase.
    infortipodeasignacion = models.CharField(db_column='INFORTipoDeAsignacion', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    infornoserie = models.CharField(db_column='INFORNoSerie', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inforformato = models.CharField(db_column='INFORFormato', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inforalmacenprod = models.CharField(db_column='INFORAlmacenProd', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    referenciaintelisisservice = models.CharField(db_column='ReferenciaIntelisisService', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    altotarima = models.FloatField(db_column='AltoTarima', blank=True, null=True)  # Field name made lowercase.
    largotarima = models.FloatField(db_column='LargoTarima', blank=True, null=True)  # Field name made lowercase.
    anchotarima = models.FloatField(db_column='AnchoTarima', blank=True, null=True)  # Field name made lowercase.
    taratarima = models.FloatField(db_column='TaraTarima', blank=True, null=True)  # Field name made lowercase.
    volumentarima = models.FloatField(db_column='VolumenTarima', blank=True, null=True)  # Field name made lowercase.
    pesotarima = models.FloatField(db_column='PesoTarima', blank=True, null=True)  # Field name made lowercase.
    cantidadcamatarima = models.FloatField(db_column='CantidadCamaTarima', blank=True, null=True)  # Field name made lowercase.
    camastarima = models.FloatField(db_column='CamasTarima', blank=True, null=True)  # Field name made lowercase.
    estibamaxima = models.IntegerField(db_column='EstibaMaxima', blank=True, null=True)  # Field name made lowercase.
    controlarticulo = models.CharField(db_column='ControlArticulo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diascontrolcaducidad = models.IntegerField(db_column='DiasControlCaducidad', blank=True, null=True)  # Field name made lowercase.
    estibamismafecha = models.BooleanField(db_column='EstibaMismaFecha', blank=True, null=True)  # Field name made lowercase.
    tiporotacion = models.CharField(db_column='TipoRotacion', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permiteestibar = models.BooleanField(db_column='PermiteEstibar', blank=True, null=True)  # Field name made lowercase.
    emidarecargatelefonica = models.BooleanField(db_column='EmidaRecargaTelefonica', blank=True, null=True)  # Field name made lowercase.
    emidatiempoaire = models.BooleanField(db_column='EmidaTiempoAire', blank=True, null=True)  # Field name made lowercase.
    articuloweb = models.CharField(db_column='ArticuloWeb', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    posforma = models.CharField(db_column='POSForma', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    esfactory = models.BooleanField(db_column='EsFactory', blank=True, null=True)  # Field name made lowercase.
    sincroid = models.TextField(db_column='SincroID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sincroc = models.IntegerField(db_column='SincroC', blank=True, null=True)  # Field name made lowercase.
    materialpeligroso = models.BooleanField(db_column='MaterialPeligroso', blank=True, null=True)  # Field name made lowercase.
    ldi = models.BooleanField(db_column='LDI', blank=True, null=True)  # Field name made lowercase.
    ldiservicio = models.CharField(db_column='LDIServicio', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tarimasreacomodar = models.IntegerField(db_column='TarimasReacomodar', blank=True, null=True)  # Field name made lowercase.
    cantidadpresentacion = models.FloatField(db_column='CantidadPresentacion', blank=True, null=True)  # Field name made lowercase.
    posagentedetalle = models.CharField(db_column='POSAgenteDetalle', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoarticulo = models.IntegerField(db_column='TipoArticulo', blank=True, null=True)  # Field name made lowercase.
    almmescoms = models.CharField(db_column='AlmMesComs', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    minimocompra = models.FloatField(db_column='MinimoCompra', blank=True, null=True)  # Field name made lowercase.
    stockminimo = models.FloatField(db_column='StockMinimo', blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.FloatField(db_column='StockMaximo', blank=True, null=True)  # Field name made lowercase.
    smr = models.IntegerField(db_column='SMR', blank=True, null=True)  # Field name made lowercase.
    crmobjectid = models.CharField(db_column='CRMObjectId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tono = models.CharField(db_column='Tono', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodproceso = models.CharField(db_column='ProdProceso', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodconsecutivo = models.CharField(db_column='ProdConsecutivo', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recuperacion = models.BooleanField(db_column='Recuperacion', blank=True, null=True)  # Field name made lowercase.
    rutaarticulo = models.BooleanField(db_column='RutaArticulo', blank=True, null=True)  # Field name made lowercase.
    prodtipoart = models.CharField(db_column='ProdTipoArt', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prodrutasecuencial = models.BooleanField(db_column='ProdRutaSecuencial', blank=True, null=True)  # Field name made lowercase.
    prodtiempoproceso = models.FloatField(db_column='ProdTiempoProceso', blank=True, null=True)  # Field name made lowercase.
    prodcapacidadinstalada = models.FloatField(db_column='ProdCapacidadInstalada', blank=True, null=True)  # Field name made lowercase.
    prodcapacidadreal = models.FloatField(db_column='ProdCapacidadReal', blank=True, null=True)  # Field name made lowercase.
    almacendes = models.CharField(db_column='AlmacenDES', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    proddestajobulto = models.FloatField(db_column='ProdDestajoBulto', blank=True, null=True)  # Field name made lowercase.
    cesumarizaenfactura = models.BooleanField(db_column='CESumarizaEnFactura', blank=True, null=True)  # Field name made lowercase.
    cenoaplicabeca = models.BooleanField(db_column='CENoAplicaBeca', blank=True, null=True)  # Field name made lowercase.
    cenoaplicaporcmat = models.BooleanField(db_column='CENoAplicaPorcMat', blank=True, null=True)  # Field name made lowercase.
    iedu = models.BooleanField(db_column='IEDU', blank=True, null=True)  # Field name made lowercase.
    meseniedu = models.BooleanField(db_column='MesEnIEDU', blank=True, null=True)  # Field name made lowercase.
    prodestructurafam = models.BooleanField(db_column='ProdEstructuraFam', blank=True, null=True)  # Field name made lowercase.
    calificacion = models.SmallIntegerField(db_column='Calificacion')  # Field name made lowercase.
    cfdiretclave = models.CharField(db_column='CFDIRetClave', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cfdiretiepsimpuesto = models.CharField(db_column='CFDIRetIEPSImpuesto', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcionhtml = models.TextField(db_column='DescripcionHTML', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicmedida = models.FloatField(db_column='vicMedida', blank=True, null=True)  # Field name made lowercase.
    vicuso = models.CharField(db_column='vicUso', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicnegociacion = models.CharField(db_column='vicNegociacion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicinmueble = models.CharField(db_column='vicInmueble', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicarea = models.CharField(db_column='vicArea', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicsubarea = models.CharField(db_column='vicSubArea', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicindiviso = models.FloatField(db_column='vicIndiviso', blank=True, null=True)  # Field name made lowercase.
    vicfactor1 = models.FloatField(db_column='vicFactor1', blank=True, null=True)  # Field name made lowercase.
    vicfactor2 = models.FloatField(db_column='vicFactor2', blank=True, null=True)  # Field name made lowercase.
    vicfactor3 = models.FloatField(db_column='vicFactor3', blank=True, null=True)  # Field name made lowercase.
    vicmesesrelcomer = models.IntegerField(db_column='vicMesesRelComer', blank=True, null=True)  # Field name made lowercase.
    vicfechaestimoper = models.DateTimeField(db_column='vicFechaEstimOper', blank=True, null=True)  # Field name made lowercase.
    vicpromplanos = models.BooleanField(db_column='vicPromPlanos', blank=True, null=True)  # Field name made lowercase.
    vicpropio = models.BooleanField(db_column='vicPropio', blank=True, null=True)  # Field name made lowercase.
    viccomplemento = models.BooleanField(db_column='vicComplemento', blank=True, null=True)  # Field name made lowercase.
    viccontratoid = models.CharField(db_column='vicContratoID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicpredial = models.CharField(db_column='vicPredial', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicnivel = models.CharField(db_column='vicNivel', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicsubnivel = models.CharField(db_column='vicSubNivel', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    viccontratoidcargoexcepcion = models.CharField(db_column='vicContratoIDCargoExcepcion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicestatus = models.CharField(db_column='vicEstatus', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicmedidaestimada = models.FloatField(db_column='vicMedidaEstimada', blank=True, null=True)  # Field name made lowercase.
    tienecontrato = models.BooleanField(db_column='TieneContrato', blank=True, null=True)  # Field name made lowercase.
    comentarios = models.TextField(db_column='Comentarios', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    proyecto = models.CharField(db_column='Proyecto', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    html = models.TextField(db_column='HTML', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    viccontratoid2 = models.IntegerField(db_column='VicContratoID2', blank=True, null=True)  # Field name made lowercase.
    vicestatus2 = models.CharField(db_column='vicEstatus2', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vicimporte1 = models.DecimalField(db_column='vicImporte1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vicimporte2 = models.DecimalField(db_column='vicImporte2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vicimporte3 = models.DecimalField(db_column='vicImporte3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vicorigen = models.CharField(db_column='vicOrigen', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    precioventam2 = models.DecimalField(db_column='PrecioVentaM2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vicfechaalta = models.DateTimeField(db_column='vicFechaAlta', blank=True, null=True)  # Field name made lowercase.
    vicventa = models.BooleanField(db_column='vicVenta', blank=True, null=True)  # Field name made lowercase.
    vicrenta = models.BooleanField(db_column='vicRenta', blank=True, null=True)  # Field name made lowercase.
    vicrentasventa = models.BooleanField(db_column='vicRentaSVenta', blank=True, null=True)  # Field name made lowercase.
    viccompra = models.BooleanField(db_column='vicCompra', blank=True, null=True)  # Field name made lowercase.
    vicsubarrendamiento = models.BooleanField(db_column='vicSubArrendamiento', blank=True, null=True)  # Field name made lowercase.
    vicintermediario = models.BooleanField(db_column='vicIntermediario', blank=True, null=True)  # Field name made lowercase.
    vicarrendamiento = models.BooleanField(db_column='vicArrendamiento', blank=True, null=True)  # Field name made lowercase.
    viccostoobra = models.DecimalField(db_column='vicCostoObra', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    viccostoterreno = models.DecimalField(db_column='vicCostoTerreno', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mfatipodeducibilidad = models.CharField(db_column='MFATipoDeducibilidad', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    escombustible = models.BooleanField(db_column='EsCombustible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Art'
    
    def __str__(self):
        return self.articulo