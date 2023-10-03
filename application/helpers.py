from application.database import TrainType
from forms.trains import LocomotiveForm, WagonForm


def list_to_form_list(
    train_list: list[tuple], train_type: TrainType
) -> list[TrainType]:
    train_form = (
        lambda data: LocomotiveForm(data=data)
        if train_type == TrainType.LOCOMOTIVE
        else WagonForm(data=data)
    )

    return list(map(train_form, train_list))
