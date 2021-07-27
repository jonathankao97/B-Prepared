part of 'home_cubit.dart';

enum HomeStatus {
  Home,
  Announcements,
  Tasks,
  Profile,
}

class HomeState extends Equatable {
  final HomeStatus status;

  const HomeState._({required this.status});

  const HomeState.Home() : this._(status: HomeStatus.Home);

  const HomeState.Announcements() : this._(status: HomeStatus.Announcements);

  const HomeState.Tasks() : this._(status: HomeStatus.Tasks);

  const HomeState.Profile() : this._(status: HomeStatus.Profile);

  @override
  List<Object> get props => [status];
}
