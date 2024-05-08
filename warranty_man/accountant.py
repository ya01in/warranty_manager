from . import warranty
import typing as T


class Accountant:
    def __init__(self) -> None:
        self._vault: T.List[warranty.Warranty] = []

    @property
    def vault(self) -> T.List[warranty.Warranty]:
        return self._vault

    def store_warranty(self, warranty: warranty.Warranty) -> None:
        self._vault.append(warranty)

    def get_valid_warranty_by_date(self, due_date) -> T.List[warranty.Warranty]:
        warranty_list: T.List[warranty.Warranty] = []
        for w in self._vault:
            due: float = w.start_date + (w.time_len_day * 86400.0)
            if due > due_date:
                warranty_list.append(w)
        return warranty_list

    def get_warranty_by_id(self, id) -> warranty.Warranty:
        for w in self._vault:
            if w.id == id:
                return w

        raise Exception(f"No warranty found with id: {id}")
