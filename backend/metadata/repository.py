def list_apps(self):
    return self.db.query(App).all()

def get_assets_by_app(self, qlik_app_id: str):
    app = self.db.query(App).filter_by(qlik_app_id=qlik_app_id).first()
    return app.assets if app else []

def approve_version(self, version_id: int):
    version = self.db.query(AssetVersion).get(version_id)
    version.status = "APPROVED"
    self.db.commit()