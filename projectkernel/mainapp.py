from . import cliapp
from .cliapp import CLIApp

from . import loadcommand
from .loadcommand import LoadCommand

from . import savecommand
from .savecommand import SaveCommand

from . import roomreservationdataaccess
from .roomreservationdataaccess import RoomReservationDataAccess

from . import commentdataaccess
from .commentdataaccess import CommentDataAccess

from . import ranchdataaccess
from .ranchdataaccess import RanchDataAccess

from . import activitydataaccess
from .activitydataaccess import ActivityDataAccess

from . import activityreservationdataaccess
from .activityreservationdataaccess import ActivityReservationDataAccess

from . import directionsdataaccess
from .directionsdataaccess import DirectionsDataAccess

from . import paymentdataaccess
from .paymentdataaccess import PaymentDataAccess

from . import travelarrangementdataaccess
from .travelarrangementdataaccess import TravelArrangementDataAccess

from . import listcommentscommand
from .listcommentscommand import ListCommentsCommand

from . import listactivitiescommand
from .listactivitiescommand import ListActivitiesCommand

from . import listroomreservationscommand
from .listroomreservationscommand import ListRoomReservationsCommand

from . import listactivityreservationscommand
from .listactivityreservationscommand import ListActivityReservationsCommand

from . import listpaymentscommand
from .listpaymentscommand import ListPaymentsCommand

from . import listdirectionscommand
from .listdirectionscommand import ListDirectionsCommand

from . import listtravelarrangementscommand
from .listtravelarrangementscommand import ListTravelArrangementsCommand

from . import printranchcommand
from .printranchcommand import PrintRanchCommand

from . import addcommentcommand
from .addcommentcommand import AddCommentCommand

from . import makeroomreservationcommand
from .makeroomreservationcommand import MakeRoomReservationCommand

from . import makeactivityreservationcommand
from .makeactivityreservationcommand import MakeActivityReservationCommand

from . import makepaymentcommand
from .makepaymentcommand import MakePaymentCommand

from . import maketravelarrangementcommand
from .maketravelarrangementcommand import MakeTravelArrangementCommand

from . import updateranchcommand
from .updateranchcommand import UpdateRanchCommand

from . import updatecommentcommand
from .updatecommentcommand import UpdateCommentCommand

from . import updateroomreservationcommand
from .updateroomreservationcommand import UpdateRoomReservationCommand

from . import updateactivityreservationcommand
from .updateactivityreservationcommand import UpdateActivityReservationCommand

from . import updatepaymentcommand
from .updatepaymentcommand import UpdatePaymentCommand

from . import deletecommentcommand
from .deletecommentcommand import DeleteCommentCommand

from . import deleteroomreservationcommand
from .deleteroomreservationcommand import DeleteRoomReservationCommand

from . import deleteactivityreservationcommand
from .deleteactivityreservationcommand import DeleteActivityReservationCommand

from . import deletepaymentcommand
from .deletepaymentcommand import DeletePaymentCommand

class MainApp(CLIApp):
    def __init__(self):
        CLIApp.__init__(self)
        self.m_RoomReservationDA = RoomReservationDataAccess("./data/RoomReservation.ini")
        self.m_CommentDA = CommentDataAccess("./data/Comment.ini")
        self.m_RanchDA = RanchDataAccess("./data/Ranch.ini")
        self.m_ActivityDA = ActivityDataAccess("./data/Activity.ini")
        self.m_ActivityReservationDA = ActivityReservationDataAccess("./data/ActivityReservation.ini")
        self.m_DirectionDA = DirectionsDataAccess("./data/Map.ini")
        self.m_PaymentDA = PaymentDataAccess("./data/Payment.ini")
        self.m_TravelArrangementDA = TravelArrangementDataAccess("./data/TravelArrangement.ini")

        loadCommand = LoadCommand(
                self.m_RoomReservationDA,
                self.m_CommentDA,
                self.m_RanchDA,
                self.m_ActivityDA,
                self.m_ActivityReservationDA,
                self.m_DirectionDA,
                self.m_PaymentDA,
                self.m_TravelArrangementDA)
        saveCommand = SaveCommand(
                self.m_RoomReservationDA,
                self.m_CommentDA,
                self.m_RanchDA,
                self.m_ActivityDA,
                self.m_ActivityReservationDA,
                self.m_DirectionDA,
                self.m_PaymentDA,
                self.m_TravelArrangementDA)
        printRanchCommand = PrintRanchCommand(self.m_RanchDA)
        listCommentsCommand = ListCommentsCommand(self.m_CommentDA)
        listActivitiesCommand = ListActivitiesCommand(self.m_ActivityDA)
        listRoomReservationsCommand = ListRoomReservationsCommand(self.m_RoomReservationDA)
        listActivityReservationsCommand = ListActivityReservationsCommand(self.m_ActivityReservationDA)
        listDirectionsCommand = ListDirectionsCommand(self.m_DirectionDA)
        listPaymentsCommand = ListPaymentsCommand(self.m_PaymentDA)
        listTravelArrangementsCommand = ListTravelArrangementsCommand(self.m_TravelArrangementDA)
        addCommentCommand = AddCommentCommand(self.m_CommentDA)
        makeRoomReservationCommand = MakeRoomReservationCommand(self.m_RoomReservationDA)
        makeActivityReservationCommand = MakeActivityReservationCommand(self.m_ActivityReservationDA)
        makePaymentCommand = MakePaymentCommand(self.m_PaymentDA)
        makeTravelArrangementCommand = MakeTravelArrangementCommand(self.m_TravelArrangementDA)
        updateRanchCommand = UpdateRanchCommand(self.m_RanchDA)
        updateCommentCommand = UpdateCommentCommand(self.m_CommentDA)
        updateRoomReservationCommand = UpdateRoomReservationCommand(self.m_RoomReservationDA)
        updateActivityReservationCommand = UpdateActivityReservationCommand(self.m_ActivityReservationDA)
        updatePaymentCommand = UpdatePaymentCommand(self.m_PaymentDA)
        deleteCommentCommand = DeleteCommentCommand(self.m_CommentDA)
        deleteRoomReservationCommand = DeleteRoomReservationCommand(self.m_RoomReservationDA)
        deleteActivityReservationCommand = DeleteActivityReservationCommand(self.m_ActivityReservationDA)
        deletePaymentCommand = DeletePaymentCommand(self.m_PaymentDA)

        self.m_commands.append(saveCommand)
        self.m_commands.append(loadCommand)
        self.m_commands.append(printRanchCommand)
        self.m_commands.append(listCommentsCommand)
        self.m_commands.append(listActivitiesCommand)
        self.m_commands.append(listRoomReservationsCommand)
        self.m_commands.append(listActivityReservationsCommand)
        self.m_commands.append(listPaymentsCommand)
        self.m_commands.append(listDirectionsCommand)
        self.m_commands.append(listTravelArrangementsCommand)
        self.m_commands.append(addCommentCommand)
        self.m_commands.append(makeRoomReservationCommand)
        self.m_commands.append(makeActivityReservationCommand)
        self.m_commands.append(makePaymentCommand)
        self.m_commands.append(makeTravelArrangementCommand)
        self.m_commands.append(updateRanchCommand)
        self.m_commands.append(updateCommentCommand)
        self.m_commands.append(updateRoomReservationCommand)
        self.m_commands.append(updateActivityReservationCommand)
        self.m_commands.append(updatePaymentCommand)
        self.m_commands.append(deleteCommentCommand)
        self.m_commands.append(deleteRoomReservationCommand)
        self.m_commands.append(deleteActivityReservationCommand)
        self.m_commands.append(deletePaymentCommand)