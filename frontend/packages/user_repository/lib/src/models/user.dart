import 'package:backend_client/backend_client.dart';

class User {
  final int pk;
  final String email;
  final String firstName;
  final String lastName;

  const User({
    required this.pk,
    required this.email,
    required this.firstName,
    required this.lastName,
  });

  static const anonymous = User(
    pk: 0,
    email: '',
    firstName: '',
    lastName: '',
  );

  static User fromUserResponse(UserResponse userResponse) {
    return User(
      pk: userResponse.pk,
      email: userResponse.email,
      firstName: userResponse.first_name,
      lastName: userResponse.last_name,
    );
  }
}
