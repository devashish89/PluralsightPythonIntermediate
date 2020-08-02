def make_bic_code(owner_code, serialNo, category="U"):
    return owner_code+category+str(serialNo).zfill(6)