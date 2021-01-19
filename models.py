from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Entity(db.Model):
    __tablename__ = 'entities_types'
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String())
    source = db.Column(db.String())
    features_periodic = db.Column(db.String())
    formula_periodic = db.Column(db.String())
    features_realtime = db.Column(db.String())
    formula_realtime = db.Column(db.String())
    result_count = db.Column(db.Integer())

    def __init__(self, id, name, source, features_periodic, formula_periodic,
                 features_realtime, formula_realtime, result_count):
        self.id = id
        self.name = name
        self.source = source 
        self.features_periodic = features_periodic
        self.formula_periodic = formula_periodic
        self.features_realtime = features_realtime
        self.formula_realtime = formula_realtime
        self.result_count = result_count

    def __reprt__(self):
        return f"""{self.id}. {self.name}:
         source: {self.source}
         features_periodic: {self.features_periodic} \
             formula_period: {self.formula_periodic}
         features_realtime: {self.features_realtime} \
             formula_realtime: {self.formula_realtime}        
         result_count: {self.result_count}
        """
        