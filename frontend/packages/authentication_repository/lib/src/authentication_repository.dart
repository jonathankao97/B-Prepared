import 'package:backend_client/backend_client.dart';

enum UserAuthenticationStatus {
  unknown,
  signedIn,
  signedOut,
}

class AuthenticationRepository {
  AuthenticationRepository(BackendClient backendClient)
      : _backendClient = backendClient;

  final BackendClient _backendClient;

  Stream<UserAuthenticationStatus> get authenticationStatus {
    return _backendClient.authenticationStatus.map((status) {
      switch (status) {
        case AuthenticationStatus.unauthenticated:
          return UserAuthenticationStatus.signedOut;
        case AuthenticationStatus.authenticated:
          return UserAuthenticationStatus.signedIn;
        case AuthenticationStatus.initial:
          return UserAuthenticationStatus.unknown;
      }
    });
  }

  Future<void> signIn({
    required String username,
    required String password,
  }) async {
    await _backendClient.authenticate(
      email: username,
      password: password,
    );
  }

  Future<void> signOut() async {
    await _backendClient.unauthenticate();
  }
}
