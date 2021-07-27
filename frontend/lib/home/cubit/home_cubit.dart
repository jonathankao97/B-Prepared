import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';

part 'home_state.dart';

class HomeCubit extends Cubit<HomeState> {
  HomeCubit() : super(HomeState.Home());

  void homeToggled() {
    emit(HomeState.Home());
  }

  void announcementsToggled() {
    emit(HomeState.Announcements());
  }

  void tasksToggled() {
    emit(HomeState.Tasks());
  }

  void profileToggled() {
    emit(HomeState.Profile());
  }
}
